const React = require('react');

class Footer extends React.Component {
  render() {
    return (
      <footer className="nav-footer" id="footer">
        <img
          src={`${this.props.config.baseUrl}img/logo_dark.png`}
          alt="Undefined Labs"
          width="226"
        />
        <section className="copyright">{this.props.config.copyright}</section>
      </footer>
    );
  }
}

module.exports = Footer;
