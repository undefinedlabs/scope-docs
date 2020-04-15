const siteConfig = {
  title: "Scope",
  tagline: "Scope documentation",
  url: "https://docs.scope.dev",
  baseUrl: "/",
  projectName: "docs",
  organizationName: "undefinedlabs",
  headerLinks: [],
  favicon: "img/favicon.png",
  headerIcon: "img/logo-scope.svg",
  colors: {
    primaryColor: "#282F4E",
    secondaryColor: "#4433D0",
  },
  copyright: `© ${new Date().getFullYear()} Undefined Labs, Inc.`,
  highlight: {
    theme: "default",
  },
  onPageNav: "separate",
  cleanUrl: true,
  enableUpdateTime: true,
  disableHeaderTitle: true,
  editUrl: "https://github.com/undefinedlabs/scope-docs/edit/master/docs/",
  docsSideNavCollapsible: true,
  usePrism: true,
  stylesheets: [
    "https://fonts.googleapis.com/css?family=Noto+Sans:400,700&display=swap",
    "https://fonts.googleapis.com/css?family=Maven+Pro:400,700&display=swap",
  ],
  gaTrackingId: "UA-112562098-10",
};

module.exports = siteConfig;
