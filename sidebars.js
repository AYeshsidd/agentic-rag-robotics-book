/**
 * Creating a sidebar enables you to:
 * - Create an ordered group of docs
 * - Render a sidebar for each doc of that group
 * - Hides the docs from the docs homepage (only shows them in the sidebar)
 * - Makes other optional features available
 *
 * Learn more: https://docusaurus.io/docs/sidebar
 */

// @ts-check

/** @type {import('@docusaurus/plugin-content-docs').SidebarsConfig} */
const sidebars = {
  textbookSidebar: [
    {
      type: 'category',
      label: 'Module 1: The Robotic Nervous System (ROS 2)',
      link: {type: 'doc', id: 'ros2-nervous-system/chapter1'},
      items: [
        'ros2-nervous-system/chapter1',
        'ros2-nervous-system/chapter2',
        'ros2-nervous-system/chapter3',
      ],
    },
    {
      type: 'category',
      label: 'Module 2: The Digital Twin (Gazebo & Unity)',
      link: {type: 'doc', id: 'digital-twin-gazebo-unity/chapter1'},
      items: [
        'digital-twin-gazebo-unity/chapter1',
        'digital-twin-gazebo-unity/chapter2',
        'digital-twin-gazebo-unity/chapter3',
      ],
    },
    {
      type: 'category',
      label: 'Module 3: The AI-Robot Brain (NVIDIA Isaac™)',
      link: {type: 'doc', id: 'ai-robot-brain-isaac/chapter1'},
      items: [
        'ai-robot-brain-isaac/chapter1',
        'ai-robot-brain-isaac/chapter2',
        'ai-robot-brain-isaac/chapter3',
      ],
    },
    {
      type: 'category',
      label: 'Module 4: Vision-Language-Action (VLA)',
      link: {type: 'doc', id: 'vision-language-action-vla/chapter1'},
      items: [
        'vision-language-action-vla/chapter1',
        'vision-language-action-vla/chapter2',
        'vision-language-action-vla/chapter3',
      ],
    },
  ],
};

module.exports = sidebars;
