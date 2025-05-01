import React from "react";
import { useLocation } from "react-router-dom";
import "./Results.css";

const ResultsPage = () => {
  const location = useLocation();
  const { rankings, results } = location.state || { rankings: {}, results: [] };

  return (
    <div className="results-container">
      <div className="user-rankings">
        <h2>My Ranking:</h2>
        {Object.entries(rankings).map(([feature, value]) => (
          <div className="ranking-row" key={feature}>
            <span className="ranking-label">{feature.replace("_", " ")}:</span>
            <span className="ranking-value">{value}</span>
          </div>
        ))}
      </div>

      <div className="recommendation-panel">
        <h2>Best Recommendations For You:</h2>
        {results.length === 0 ? (
          <p>(Laptop cards or results will be shown here soon...)</p>
        ) : (
          results.map((laptop, index) => (
            <div key={index} className="ranking-row">
              <span className="ranking-label">
                {laptop["Laptop Name"]}
              </span>
              <span className="ranking-value">
                CPU: {laptop["CPU"]} | GPU: {laptop["Graphic Card"]} | RAM: {laptop["RAM"]} GB | 
                Storage: {laptop["Storage"]} GB | Screen: {laptop["Screen Size"]} in | 
                OS: {laptop["Operating System"]} | Brand: {laptop["Brand"]} | 
                Color: {laptop["Color"]} | Weight: {laptop["Weight"]} kg | 
                Memory Speed: {laptop["Memory Speed"]} MHz | Price: {laptop["Price"]} ₺
                <br />
                <strong>Correctness Score: {laptop["Correctness Score (%)"]}%</strong>
              </span>
            </div>
          ))
        )}
      </div>
    </div>
  );
};

export default ResultsPage;