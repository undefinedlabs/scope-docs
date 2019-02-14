/**
 * Copyright (c) 2017-present, Facebook, Inc.
 *
 * This source code is licensed under the MIT license found in the
 * LICENSE file in the root directory of this source tree.
 */

// See https://docusaurus.io/docs/site-config for all the possible
// site configuration options.

const siteConfig = {
  title: 'Scope',
  tagline: 'Scope documentation',
  url: 'https://scope.undefinedlabs.com',
  baseUrl: '/',
  projectName: 'docs',
  organizationName: 'undefinedlabs',
  headerLinks: [],
  favicon: 'img/favicon.png',
  colors: {
    primaryColor: '#282F4E',
    secondaryColor: '#4433D0',
  },
  copyright: `Copyright © ${new Date().getFullYear()} Undefined Labs, Inc.`,
  highlight: {
    theme: 'default',
  },
  onPageNav: 'separate',
  cleanUrl: true,
  ogImage: 'img/docusaurus.png',
  twitterImage: 'img/docusaurus.png',
  enableUpdateTime: true,
};

module.exports = siteConfig;
