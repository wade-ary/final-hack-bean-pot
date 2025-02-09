// src/InfoSection.js
import React from "react";
import "./HomeInfo.css"; // Import the CSS for styling

const HomeInfo = () => {
  return (
    <section className="info-section">
      {/* Left side: Image */}
      <div className="info-image">
        {/* Make sure the image exists in your public folder or update the path accordingly */}
        <img src="/picture.png" alt="Description of the image" />
      </div>

      {/* Right side: Content */}
      <div className="info-content">
        <div className="info-item">
          <div className="info-icon">
            {/* You can use an <img>, an icon component, or even a font icon */}
            <img src="/calendar.svg" alt="Icon 1" />
          </div>
          <p>This is the first paragraph of text explaining something important.</p>
        </div>
        <div className="info-item">
          <div className="info-icon">
            <img src="/luggage.svg" alt="Icon 2" />
          </div>
          <p>This is the second paragraph of text that provides more details.</p>
        </div>
        <div className="info-item">
          <div className="info-icon">
            <img src="/activity.svg" alt="Icon 3" />
          </div>
          <p>This is the third paragraph of text with additional information.</p>
        </div>
        <div className="info-item">
          <div className="info-icon">
            <img src="/car.svg" alt="Icon 4" />
          </div>
          <p>This is the fourth paragraph of text to wrap up the section.</p>
        </div>
      </div>
    </section>
  );
};

export default HomeInfo;
