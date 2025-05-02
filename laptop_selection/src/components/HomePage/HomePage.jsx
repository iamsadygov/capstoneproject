import React from "react";
import { useNavigate } from "react-router-dom";
import "./HomePage.css";

const HomePage = () => {
  const navigate = useNavigate();

  return (
    <div className="home-container">
      {/* Banner Section */}
      <div className="banner">
        <div className="banner-content">
          <h1>Find Your Perfect Laptop in Minutes</h1>
          <button className="start-btn" onClick={() => navigate("/ranking")}>
            Start Finding My Laptop
          </button>
        </div>
      </div>

      {/* How It Works Section */}
      <div className="how-it-works">
        <h2>How It Works</h2>
        <div className="steps">
          <div className="step">
            <span className="step-number">1</span>
            <h3>Rank Your Needs</h3>
            <p>
              Prioritize the features that matter most to you. The more important a feature is to you, the higher you should rate it.
            </p>
          </div>
          <div className="step">
            <span className="step-number">2</span>
            <h3>We Analyze</h3>
            <p>
              Our system processes your preferences using a smart algorithm powered by decision analysis.
            </p>
          </div>
          <div className="step">
            <span className="step-number">3</span>
            <h3>Get Recommendations</h3>
            <p>
              We show you the best laptop options tailored to your needs — fast, easy, and reliable.
            </p>
          </div>
        </div>
      </div>
    </div>
  );
};

export default HomePage;
