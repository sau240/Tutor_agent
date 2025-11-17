// src/App.jsx
import { useState } from "react";
import "./App.css"; // Assuming your CSS is in src/styles.css

const App = () => {
  const [textInput, setTextInput] = useState("");
  const [imageFile, setImageFile] = useState(null);
  const [response, setResponse] = useState("");
  const [loading, setLoading] = useState(false); // ✅ Loading state

  const handleTextSubmit = async (e) => {
    e.preventDefault();
    setLoading(true); // start loading
    try {
      const res = await fetch("http://127.0.0.1:5000/api/text", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ text_input: textInput })
      });
      const data = await res.json();
      setResponse(data.response);
    } catch (err) {
      console.error(err);
      setResponse("Error connecting to backend");
    }
    setTextInput("");
    setLoading(false); // stop loading
  };

  const handleImageSubmit = (e) => {
    e.preventDefault();
    if (imageFile) {
      setResponse(`Image uploaded: ${imageFile.name}`);
    } else {
      setResponse("No image selected.");
    }
  };

  return (
    <div className="container">
      <h1>Shiksha Mitra</h1>
      <p>Welcome to the Shiksha Mitra application!</p>

      <form onSubmit={handleTextSubmit}>
        <label htmlFor="text_input">Answer the asked question:</label>
        <input
          type="text"
          id="text_input"
          name="text_input"
          placeholder="What is photosynthesis?"
          value={textInput}
          onChange={(e) => setTextInput(e.target.value)}
        />
        <button type="submit">Submit</button>
      </form>

      <br /><br />

      <form onSubmit={handleImageSubmit}>
        <label htmlFor="image">Upload an image:</label>
        <input
          type="file"
          id="image"
          name="image"
          accept="image/*"
          onChange={(e) => setImageFile(e.target.files[0])}
        />
        <button type="submit">Submit</button>
      </form>

      {/* ✅ Show loading if waiting for backend */}
      {loading && (
        <div className="response-container-wrapper">
          <h2 className="response-title">Loading...</h2>
          <div className="response-box">
            <p>Please wait, processing your request...</p>
          </div>
        </div>
      )}

      {response && !loading && (
        <div className="response-container-wrapper">
          <h2 className="response-title">Response:</h2>
          <div className="response-box">
            <p>{response}</p>
          </div>
        </div>
      )}

      <hr />

      <div className="footer-buttons">
        <button onClick={() => alert("Coming Soon!")}>Voice Input</button>
        <button onClick={() => alert("Coming Soon!")}>Image Upload</button>
      </div>
    </div>
  );
};

export default App;
