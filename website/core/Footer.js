import React from "react";

const Footer = ({ config: { baseUrl, copyright } }) => (
  <footer className="nav-footer" id="footer">
    <div className="wrapper">
      <a
        href="https://undefinedlabs.com"
        target="_blank"
        rel="noopener noreferrer"
      >
        <img
          src={`${baseUrl}img/logo-undefined.png`}
          alt="Undefined Labs"
          width="180"
        />
      </a>
      <section className="copyright">{copyright}</section>
    </div>
  </footer>
);

module.exports = Footer;
