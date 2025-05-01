import React, { useState } from "react";
import {
  FaWeightHanging,
  FaWindows,
  FaMemory,
  FaMicrochip,
  FaLaptop,
  FaPalette,
  FaDollarSign,
  FaExpand,
  FaRocket,
  FaShoppingBasket,
  FaHdd
} from "react-icons/fa";
import { useNavigate } from "react-router-dom";
import "./RankingPage.css";

const featureIcons = {
  Weight: <FaWeightHanging />,
  Operating_System: <FaWindows />,
  Memory_Speed: <FaMemory />,
  RAM: <FaMicrochip />,
  Graphics_Card: <FaLaptop />,
  CPU: <FaRocket />,
  Brand: <FaShoppingBasket />,
  Screen_Size: <FaExpand />,
  Color: <FaPalette />,
  Price: <FaDollarSign />,
  Storage: <FaHdd />,
};

const steps = [
  ["Weight", "Operating_System", "Memory_Speed", "RAM"],
  ["Graphics_Card", "CPU", "Storage", "Brand"],
  ["Screen_Size", "Color", "Price"]
];

const RankingPage = () => {
  const [rankings, setRankings] = useState({
    Weight: 0,
    Operating_System: 0,
    Memory_Speed: 0,
    RAM: 0,
    Graphics_Card: 0,
    CPU: 0,
    Brand: 0,
    Screen_Size: 0,
    Color: 0,
    Price: 0,
    Storage: 0,
  });

  const [currentStep, setCurrentStep] = useState(0);
  const navigate = useNavigate();

  const handleSliderChange = (feature, value) => {
    setRankings({ ...rankings, [feature]: value });
  };

  const resetAll = () => {
    const reset = {};
    Object.keys(rankings).forEach((key) => (reset[key] = 0));
    setRankings(reset);
    setCurrentStep(0);
  };

  const nextStep = () => {
    if (currentStep < steps.length - 1) {
      setCurrentStep(currentStep + 1);
    }
  };

  const prevStep = () => {
    if (currentStep > 0) {
      setCurrentStep(currentStep - 1);
    }
  };

  return (
    <div className="ranking-container">
      <div className="ranking-header">
        <p>
           <strong>Tell Us What Matters Most to You</strong>
        </p>
      </div>

      <div className="ranking-box">
        <p className="ranking-title">
          Rank the features you value most in your next laptop
        </p>

        <div className="ranking-grid">
          {steps[currentStep].map((feature, index) => (
            <div className="ranking-item" key={index}>
              <label className="ranking-label">
                {featureIcons[feature]} {feature.replace("_", " ")}:
              </label>
              <input
                type="range"
                min="0"
                max="5"
                value={rankings[feature]}
                onChange={(e) =>
                  handleSliderChange(feature, parseInt(e.target.value))
                }
                className="ranking-slider"
              />
              <div className="slider-values">
                <span>0</span>
                <span>1</span>
                <span>2</span>
                <span>3</span>
                <span>4</span>
                <span>5</span>
              </div>
            </div>
          ))}
        </div>

        <div className="ranking-button-group">
          <button className="reset-btn" onClick={resetAll}>
            Reset All
          </button>

          {currentStep > 0 && (
            <button className="ranking-btn" onClick={prevStep}>
              Back
            </button>
          )}

          {currentStep < steps.length - 1 ? (
            <button className="ranking-btn" onClick={nextStep}>
              Next
            </button>
          ) : (
            <button
              className="ranking-btn"
              onClick={async () => {
                try {
                  const response = await fetch("http://localhost:5000/recommend", {
                    method: "POST",
                    headers: { "Content-Type": "application/json" },
                    body: JSON.stringify(rankings),
                  });
              
                  const data = await response.json();
                  navigate("/results", { state: { rankings, results: data.results } });
                } catch (error) {
                  console.error("API error:", error);
                  alert("Failed to get recommendations. Is the backend running?");
                }
              }}
            >
              Show Now
            </button>
          )}
        </div>
      </div>
    </div>
  );
};

export default RankingPage;