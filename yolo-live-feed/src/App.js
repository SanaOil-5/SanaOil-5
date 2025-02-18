import React, { useState, useEffect } from "react";
import './App.css'; // Ensure you import your CSS

function App() {
  const [imageSrc, setImageSrc] = useState("http://192.168.1.3:8000/video_feed?" + new Date().getTime()); //(NEED TO CHANGE!!!) Depend on your IP address, open cmd and ip config and copy the IPv4 Address to the host

  useEffect(() => {
    const interval = setInterval(() => {
      setImageSrc("http://192.168.1.3:8000/video_feed?" + new Date().getTime()); // (NEED TO CHANGE!!!) Depend on your IP address, open cmd and ip config and copy the IPv4 Address to the host
    }, 2000); // Refresh every 2 seconds

    return () => clearInterval(interval); // Cleanup on component unmount
  }, []);

  return (
    <div className="App">
      <header className="App-header">
        <h1>Live YOLOv8 Detection</h1>
      </header>
      <div className="App-video-container">
        <img
          src={imageSrc}
          alt="YOLOv8 Live Feed"
          onError={(e) => console.log("Error loading live feed", e)}
        />
      </div>
      <footer className="App-footer">
        <p>Powered by FastAPI & React</p>
      </footer>
    </div>
  );
}

export default App;
