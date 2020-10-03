const url = 'http://127.0.0.1:5000/postData';
const form = document.querySelector('form');
// const axios = require('axios')

form.addEventListener('submit', (e) => {
  e.preventDefault();

  // const files = document.querySelector('[type=file]').files
  // const formData = new FormData()
  //
  // for (let i = 0; i < files.length; i++) {
  //   let file = files[i]
  //
  //   formData.append('files[]', file)
  // }
  // request(url);

  const filename = document.getElementById('upload')
  // console.log(filename.files[0])
  var fReader = new FileReader();
  fReader.readAsDataURL(filename.files[0]);
  rawData = "";
  fReader.onloadend = function(event){
    rawData = event.target.result;
    let axiosConfig = {
      headers: {
          'Content-Type': 'application/json'
      }
    };
    axios.post(url, {
        data : rawData
      },
      axiosConfig
    )
    .then((response) => {
      console.log(response);
    }, (error) => {
      console.log(error);
    });
  }
  console.log(fReader)


  // fetch(url, {
  //   method: 'POST',
  //   headers: {
  //     'Content-Type': 'application/json'
  //   },
  //   body:JSON.stringify({key : 'value'})
  // }).then((response) => {
  //   console.log(response)
  // })
})



async function request(req)  {
  dict = {
    'hello' : 'data'
  };
  await fetch(req, {
    method: 'POST',

    body: JSON.stringify({"data" : "hello"}),
    redirect: "follow",
    mode: "cors"
  }).then((response) => {
    console.log(response);
  });
}
