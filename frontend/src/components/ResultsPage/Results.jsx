import React from "react";
import { useLocation } from "react-router-dom";
import "./Results.css";

const ResultsPage = () => {
  const location = useLocation();
  const { rankings, results = [] } = location.state || {};

  return (
    <div className="results-screen">
      <div className="results-container">
        <div className="user-rankings">
          <h2>Ranking:</h2>
          {Object.entries(rankings).map(([feature, value]) => (
            <div className="ranking-row" key={feature}>
              <span className="ranking-label">{feature.replace("_", " ")}:</span>
              <span className="ranking-value">{value}</span>
            </div>
          ))}
        </div>

        <div className="recommendation-panel">
          {results.length > 0 ? (
            <>
              <h2>Laptops recommender for you:</h2>
              <div className="results-grid">
                {results.map((laptop, index) => (
                  <div key={index} className="laptop-card">
                    <h3>{laptop["Laptop Name"]}</h3>
                    <ul className="laptop-specs">
                      <li>CPU: {laptop["CPU"]}</li>
                      <li>GPU: {laptop["Graphic Card"]}</li>
                      <li>RAM: {laptop["RAM"]} GB</li>
                      <li>Storage: {laptop["Storage"]} GB</li>
                      <li>Screen: {laptop["Screen Size"]} in</li>
                      <li>OS: {laptop["Operating System"]}</li>
                      <li>Brand: {laptop["Brand"]}</li>
                      <li>Color: {laptop["Color"]}</li>
                      <li>Weight: {laptop["Weight"]} kg</li>
                      <li>Memory Speed: {laptop["Memory Speed"]}</li>
                      <li>Price: {laptop["Price"]} ₺</li>
                    </ul>
                  </div>
                ))}
              </div>
            </>
          ) : (
            <p>No recommendations found for the given preferences.</p>
          )}
        </div>
      </div>
    </div>
  );
};

export default ResultsPage;
