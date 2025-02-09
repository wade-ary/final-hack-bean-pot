// src/Home.js
import React from "react";
import HomeHero from "./HomeHero";
import HomeInfo from "./HomeInfo";
import HomeInfo2 from "./HomeInfo2";
import HomeInfo3 from "./HomeInfo3";
import HomeOutro from "./HomeOutro";

function Home() {
  return (
    <div>
      <HomeHero />
      <HomeInfo />
      <HomeInfo3 />
      <HomeInfo2 />
      <HomeOutro />
    </div>
  );
}

export default Home;
