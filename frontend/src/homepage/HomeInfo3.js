// src/HomeInfo3.js
import React from "react";
import "./HomeInfo3.css";

const HomeInfo3 = () => {
  return (
    <section className="info-section3">
      {/* Top: Centered Text */}
      <div className="info-text3">
        <h1>Header 1</h1> 
        <p>This is the first paragraph of text explaining something important.</p>
      </div>

      {/* Bottom: Row of Images */}
      <div className="info-image3">
        <img src="/picture.png" alt="Description of the image 1" />
        <img src="/picture.png" alt="Description of the image 2" />
        <img src="/picture.png" alt="Description of the image 3" />
      </div>
    </section>
  );
};

export default HomeInfo3;

