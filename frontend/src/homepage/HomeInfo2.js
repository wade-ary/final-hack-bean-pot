// src/InfoSection.js
import React from "react";
import "./HomeInfo2.css"; // Import the CSS for styling

const HomeInfo2 = () => {
  return (
    <section className="info-section2">
      {/* Left side: Content */}
      <div className="info-content2">
        <div className="info-item2">
          <div className="info-icon2">
            <h1>Header 1</h1> 
          </div>
          <p>This is the first paragraph of text explaining something important.</p>
        </div>
        <div className="info-item2">
          <div className="info-icon2">
          <h1>Header 2</h1> 
          </div>
          <p>This is the second paragraph of text that provides more details.</p>
        </div>
        <div className="info-item2">
          <div className="info-icon2">
          <h1>Header 3</h1> 
          </div>
          <p>This is the third paragraph of text with additional information.</p>
        </div>
        <div className="info-item2">
          <div className="info-icon2">
          <h1>Header 4</h1> 
          </div>
          <p>This is the fourth paragraph of text to wrap up the section.</p>
        </div>
      </div>

      {/* Right side: Image */}
      <div className="info-image2">
        {/* Make sure the image exists in your public folder or update the path accordingly */}
        <img src="/picture.png" alt="Description of the image" />
      </div>

    </section>
  );
};

export default HomeInfo2;
