const url = 'http://127.0.0.1:5000/postData';
const form = document.querySelector('form');
// const axios = require('axios')

fileLocation = 'C:\Users\bunne\Desktop\hackathons\musicalNoteRecognition'
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
  var timeArray = [];
  var noteArray = [];
  var octaveArray = [];
  const filename = document.getElementById('upload')
  // console.log(filename.files[0])
  var fReader = new FileReader();
  fReader.readAsDataURL(filename.files[0]);
  console.log(filename.files[0].name);
  rawData = "";
  fReader.onloadend = function(event){
    rawData = event.target.result;
    let axiosConfig = {
      headers: {
          'Content-Type': 'application/json'
      }
    };
    axios.post(url, {
        name : String(filename.files[0].name),
        upload : 1
      },
      axiosConfig
    )
    .then((response) => {
      console.log(response);

      document.getElementById("myHeader").innerHTML = response.data.identify;
      timeArray = response.data.time;
      noteArray = response.data.notes;
      octaveArray = response.data.octave;
      console.log(octaveArray)
      let finalAudio = document.getElementById('finalAudio');
      // console.log(finalAudio.src.split('index.html')[0])
      finalAudio.src = finalAudio.src.split('index.html')[0] + filename.files[0].name //setting final audio player to uploaded song

    }, (error) => {
      console.log(error);
    });
  }
  console.log(fReader)
  console.log('hello')
  var aud = document.getElementById("finalAudio");
  aud.ontimeupdate = function() {myFunction()};
  function myFunction() {
    // Display the current position of the audio in a p element with id="demo"
    for (let x = 0; x < timeArray.length; x++) {
      // console.log(aud.currentTime);
      if (aud.currentTime <= timeArray[x] * 2.265486e-5) {
        // console.log(chordArray[x])
        document.getElementById("demo").innerHTML = String(noteArray[x]) + ". " + String(octaveArray[x]) + " octaves away from middle C.";
        break;
      }
    }
    // document.getElementById("demo").innerHTML = String(aud.currentTime.toFixed(1)) + ' hello';
  }
})
