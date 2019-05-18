
//================= Query Selectors========================================
let product_selection = document.querySelector("#product_selection")
let submit_product = document.querySelector("#submit_product")
let selection = document.querySelector("#selection")
let rei = document.getElementById("rei")
let rei_para = document.getElementById("rei_para")
let number = document.getElementById("epa_number")
let btn_save = document.querySelector('#btn_save')
let cancel = document.querySelector('#cancel')




{% extends 'blog/polygon.html' %}

// ================Styling=================================================
product_selection.classList.add('select_style')
selection.classList.add('select_style')

let selected_location_id = null
var color = 0;
function initMap() {
  let locations = [
  {% for location in locations %}
    {
      id: {{location.id}},
      name: '{{location.name}}',
      vertices: [{{location.verticies}}],
      restricted: {% if location.is_restricted %}true{% else %}false {% endif %}
    },
  {% endfor %}
  ]

  var siteColors = ['000000', '#FF0000', '#7CFC00']

  var map = new google.maps.Map(document.getElementById('map'), {
    zoom: 18,
    minZoom: 18,
    maxZoom: 18,
    center: {lat: 45.147124, lng: -122.760927},
    mapTypeId: 'satellite',
    zoomControl: false,
    streetViewControl: false,
    fullscreenControl: false,
    mapTypeControl: false,
  })

  for (let i=0; i<locations.length; i++) {
    let location = locations[i];
    var centroidLat = 0;
    var centroidLng = 0;
    let verticesArray = []
    for (var j=0; j<location.vertices.length; j += 2){
      let lat = location.vertices[j]
      let lng = location.vertices[j+1]
      verticesArray.push(new google.maps.LatLng(lat, lng))
      centroidLat += lat;
      centroidLng += lng;
    }

    var cent = new google.maps.LatLng(centroidLat/verticesArray.length, centroidLng/verticesArray.length);
    var greenhousePolygon = new google.maps.Polygon({
      paths: verticesArray,
      strokeColor: "#FF0000",
      strokeOpacity: 0.5,
      strokeWeight: 1,
      fillColor: location.restricted? 'red': "#000000",
      fillOpacity: 0.20,
      position: cent,
      map:map
    });
    click(greenhousePolygon, location);
    {% if user.is_staff %}
      cancel_modal(greenhousePolygon)
    {%endif%}
  }
}

  //---------------------- changes colors of polygons ----------------------
  //------if color changes red, the modal becomes available by dblclick-----

  function click(greenhousePolygon, location) {

      var listener = google.maps.event.addListener(greenhousePolygon, 'click', function(){
      {% if user.is_staff %}
        console.log(location["name"])
        greenhousePolygon.setOptions({fillColor:"#FF0000"});
      {%endif%}
    $('#map').on('dblclick', function (e) {
      $('#exampleModalCenter').modal('toggle');
      $("#SiteName").text(location.name)
      selected_location_id = location.id
      })
    })
  }
  function cancel_modal(greenhousePolygon, listener){
    cancel.addEventListener("click", function(){
      greenhousePolygon.setOptions({fillColor:"#000000"});
    })
  }



  //---------------------- Hides modal button --------------------------
  $(".btn-primary").hide();
  //---------------------- Modal Purpose selection ------------------------
  {% if user.is_staff %}
    let option = null
    {% for use in uses %}
      option = document.createElement("option")
      option.text = "{{use.use}}"
      option.value = {{use.id}}
      selection.appendChild(option)
    {%endfor%}

  {%endif%}

  //---------------------- Modal Pesticide selection ------------------------
  // ----------------------Takes user input from use selection to filter full pesticide list
  selection.addEventListener("change", function(){
    var use_choice = $('#selection option:selected').text();
    product_selection.innerHTML = '';
    {% for pesticide in datas %};
      if ("{{pesticide.use}}" == use_choice){
        let option = document.createElement("option")
        option.text = "{{pesticide.product_name}}"
        option.value = {{pesticide.id}}
        product_selection.appendChild(option)
      };
    {% endfor %};
  });




  //---------------------- Modal Pesticide Popover initiator ------------------------
  submit_product.addEventListener("click", function(){
    $(function() {
      $('[data-toggle="popover"]').popover()
    })
    // ---------------------- Ajax call------------------
    // ----------- pulls pesticide data and compares it product choice.  ithen populates the popover with the correct informaiton.-----

    let config = {
      headers: {
        'X-CSRFToken': '{{ csrf_token }}'
      }
    }
    axios.get('{% url 'rup:get_product' %}', config)
    .then(function(response) {
      var data = response.data;
      var popover = $('.btn-danger').data('bs.popover');
      var product_choice = $('#product_selection option:selected').text()
      for (let i=0; i < data.products.length; i++) {

        if (product_choice == data.products[i].product_name){
          $('button').attr('data-content', data.products[i].rui);
          popover.setContent();
          number.innerText = data.products[i].epa_number
        }
      }
    })
  })


  // ---------------------- Modal REI set time ------------------------



  // function getPrettyDate(date) {
  //   let ampm = ''
  //   if (h.getHours() < 12) {
  //     ampm = 'AM'
  //   } else {
  //     ampm = 'PM'
  //   }
  //   let h = date.getHours() % 12;
  //   if (h == 0) {
  //     h += 12
  //   }
  //   let m = date.getMinutes();
  //   if (m < 10) {
  //     m = "0" + m
  //   }
  //   return `${h} : ${m} ${ampm}`
  let JSONdate = null
  let JSONdate_input = null


  rei.addEventListener("click", function() {
     rei_click()
  })

  function rei_click(){

    let rei_input = document.getElementById("rei_input").value
    let date_time = new Date()

    let date = date_time.toLocaleDateString();
    let rei_input_int = parseInt(rei_input)


    if (rei_input_int >= 24){
      let day = (date_time.getDate() + rei_input_int/24)
      date_time.setDate(day)
    }

    let rei_date = date_time.toLocaleDateString()
    let ampm = ""
    if (date_time.getHours() < 12){ampm = 'AM'} else {ampm = 'PM'}
    let h = date_time.getHours() % 12;
    if (h == 0){h += 12}
    let m = date_time.getMinutes();
    if (m < 10){m = "0" + m;}
    let time = `${h} : ${m} ${ampm}`


    let yyyy = date_time.getFullYear()
    let mm = date_time.getMonth()+1
    if (mm < 12){mm = "0" + mm;}
    let dd = date_time.getDate()
    if (dd < 10){dd = "0" + dd;}
    let dd_rei = date_time.getDate()
    if (dd_rei < 10){dd_rei = "0" + dd_rei;}
    let hh = date_time.getHours()
    if (hh < 10){hh = "0" + hh;}
    let min = date_time.getMinutes()
    if (min < 10){min = "0" + min;}
    let ss = date_time.getSeconds()
    if (ss < 10){ss = "0" + ss;}
    let uuu = date_time.getMilliseconds()
    let tz = '0'+ date_time.getTimezoneOffset()/60 + ':00'

    JSONdate = `${yyyy}`+'-'+`${mm}`+'-'+`${dd}`+' '+`${hh}`+':'+`${min}`+':'+`${ss}`+'.'+`${uuu}`+'000'+'-'+`${tz}`

    let h_rei_int = date_time.setHours(date_time.getHours() + rei_input_int);
    let h_rei = new Date(h_rei_int)
    if (h_rei.getHours() < 12){let ampm = 'AM'} else {ampm = 'PM'}
    h_rei = h_rei.getHours() % 12;
    if (h_rei == 0){h_rei+= 12}
    let rei_time = `${h_rei} : ${m} ${ampm}`

    rei_para.innerText = "Applied on "+date+ " at "+time + '\n' + "Stay out until "+rei_date+ " at "+rei_time

    if (rei_input_int >= 24){
      dd_rei = (date_time.getDate() + rei_input_int/24)
      date_time.setDate(dd_rei)
    }
    let hh_rei = h_rei + 12
    if (hh_rei < 10){hh_rei = "0" + hh_rei}

    JSONdate_rei = `${yyyy}`+'-'+`${mm}`+'-'+`${dd_rei}`+' '+`${hh_rei}`+':'+`${min}`+':'+`${ss}`+'.'+`${uuu}`+'000'+'-'+`${tz}`

    console.log(JSONdate)
    console.log(JSONdate_rei)
  }

  // -------------------Save Data----------------------------------

  btn_save.addEventListener("click", function(){

    pesticide_id = product_selection.options[product_selection.selectedIndex].value
    let data = {
      'start': JSONdate,
      'end': JSONdate_rei,
      'pesticide_id': pesticide_id,
      'location_id': selected_location_id
    }
    let config = {
      headers: {
        'X-CSRFToken': '{{ csrf_token }}'
      }
    }
    axios.post("{% url 'rup:modal' %}", data, config)
    .then(function(response) {
      console.log(response.data)
    })
  })
