// @ts-check
// Note: type annotations allow type checking and IDEs autocompletion

const lightCodeTheme = require('prism-react-renderer/themes/github');
const darkCodeTheme = require('prism-react-renderer/themes/dracula');

/** @type {import('@docusaurus/types').Config} */
const config = {
  title: 'Unified Textbook for Teaching Physical AI & Humanoid Robotics',
  tagline: 'A structured learning resource for students, detailing the end-to-end development of humanoid robotic systems—from physical intelligence and perception to control, simulation, and real-world deployment.',
  favicon: 'img/favicon.ico',

  // Set the production url of your site here
  url: 'https://your-docusaurus-site.example.com',
  // Set the /<baseUrl>/ pathname under which your site is served
  // For GitHub pages deployment, it is often '/<projectName>/'
  baseUrl: '/',

  // GitHub pages deployment config.
  // If you aren't using GitHub pages, you don't need these.
  organizationName: 'Physical-AI-Book', // Usually your GitHub org/user name.
  projectName: 'physical-ai-book', // Usually your repo name.

  onBrokenLinks: 'throw',
  onBrokenMarkdownLinks: 'warn',

  // Even if you don't use internalization, you can use this field to set useful
  // metadata like html lang. For example, if your site is Chinese, you may want
  // to replace "en" with "zh-Hans".
  i18n: {
    defaultLocale: 'en',
    locales: ['en'],
  },

  presets: [
    [
      'classic',
      /** @type {import('@docusaurus/preset-classic').Options} */
      ({
        docs: {
          sidebarPath: require.resolve('./sidebars.js'),
          // Please change this to your repo.
          // Remove this to remove the "edit this page" links.
          editUrl:
            'https://github.com/Physical-AI-Book/physical-ai-book/tree/main/',
        },
        blog: {
          showReadingTime: true,
          // Please change this to your repo.
          // Remove this to remove the "edit this page" links.
          editUrl:
            'https://github.com/Physical-AI-Book/physical-ai-book/tree/main/',
        },
        theme: {
          customCss: require.resolve('./src/css/custom.css'),
        },
      }),
    ],
  ],

  themeConfig:
    /** @type {import('@docusaurus/preset-classic').ThemeConfig} */
    ({
      // Replace with your project's social card
      image: 'img/docusaurus-social-card.jpg',
      navbar: {
        style:"dark",
        title: 'Physical AI & Humanoid Robotics',
        logo: {
          alt: '',
          src: 'img/logo.svg',
        },
        items: [
          {
            type: 'docSidebar',
            sidebarId: 'textbookSidebar',
            position: 'left',
            label: 'Textbook',
          },
          
          {
            href: 'https://github.com/Physical-AI-Book/physical-ai-book',
            label: 'GitHub',
            position: 'right',
          },
        ],
      },
      footer: {
        style: 'dark',
        links: [
          {
            title: 'Explore Book',
            items: [
              {
                label: 'Module 1: Ros_2',
                to: '/docs/ros2-nervous-system/chapter1',
              },
               {
                label: 'Module 2: Digital Twin',
                to: '/docs/digital-twin-gazebo-unity/chapter1',
              },
              {
                label: 'Module 3: Ai-Robot Brain',
                to: '/docs/ai-robot-brain-isaac/chapter1',
              },
              {
                label: 'Module 4: Voice To Action',
                to: '/docs/vision-language-action-vla/chapter1',
              },
            ],
          },
          {
            title: 'Useful Resources',
            items: [
              {
                label: 'ROS_2 Developers',
                href: 'https://docs.ros.org/#contribute-section',
              },
              {
                label: 'Voice to Action',
                href: 'https://platform.openai.com/docs/guides/voice-agents',
              },
              {
                label: 'Gazebo-Unity',
                href: 'https://unity.com/resources',
              },
            ],
          },
          {
            title: 'More',
            items: [
              {
                label: 'Blog',
                to: '/docs/ros2-nervous-system/chapter1',
              },
              {
                label: 'GitHub',
                href: 'https://github.com/Physical-AI-Book/physical-ai-book',
              },
            ],
          },
        ],
        copyright: `Copyright © ${new Date().getFullYear()} Physical AI Book — Ayesh Siddiqui — Built with Docusaurus.`,
      },
      prism: {
        theme: lightCodeTheme,
        darkTheme: darkCodeTheme,
      },
    }),
};

module.exports = config;
