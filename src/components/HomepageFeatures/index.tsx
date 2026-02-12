import React, { useEffect, useRef } from 'react';
import styles from './styles.module.css';

const ModuleList = [
  {
    title: 'ROS2 Fundamentals',
    description: 'Master the core concepts of ROS2 architecture, nodes, topics, and services for building robust robotic systems.',
    image: '/img/modules/ros2-basics.jpg',
    link: '/docs/ros2-nervous-system/chapter1',
  },
  {
    title: 'Sensors & Actuators',
    description: 'Explore sensor integration, data processing, and actuator control for physical AI applications.',
    image: '/img/modules/sensors-actuators.jpg',
    link: '/docs/ros2-nervous-system/chapter2',
  },
  {
    title: 'Navigation & Planning',
    description: 'Learn autonomous navigation, path planning algorithms, and obstacle avoidance techniques.',
    image: '/img/modules/navigation.jpg',
    link: '/docs/ros2-nervous-system/chapter3',
  },
  {
    title: 'Robot Manipulation',
    description: 'Understand kinematics, dynamics, and control strategies for robotic manipulation tasks.',
    image: '/img/modules/manipulation.jpg',
    link: '/docs/ai-robot-brain-isaac/chapter1',
  },
  {
    title: 'Computer Vision',
    description: 'Implement perception systems using computer vision and deep learning for robotics.',
    image: '/img/modules/perception.jpg',
    link: '/docs/vision-language-action-vla/chapter1',
  },
  {
    title: 'AI Integration',
    description: 'Integrate machine learning models and AI algorithms into robotic systems.',
    image: '/img/modules/ai-integration.jpg',
    link: '/docs/vision-language-action-vla/chapter2',
  },
];

function ModuleCard({ title, description, image, link }) {
  const cardRef = useRef(null);

  useEffect(() => {
    const observer = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          if (entry.isIntersecting) {
            entry.target.classList.add(styles.visible);
          }
        });
      },
      {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px',
      }
    );

    if (cardRef.current) {
      observer.observe(cardRef.current);
    }

    return () => {
      if (cardRef.current) {
        observer.unobserve(cardRef.current);
      }
    };
  }, []);

  return (
    <div ref={cardRef} className={styles.moduleCard}>
      <a href={link} className={styles.cardLink}>
        <div className={styles.imageContainer}>
          {image && (
            <img
              src={image}
              alt={`${title} - Learn about ${description.split('.')[0].toLowerCase()}`}
              className={styles.moduleImage}
              loading="lazy"
              onError={(e) => {
                e.currentTarget.style.display = 'none';
                const placeholder = e.currentTarget.nextElementSibling;
                if (placeholder) {
                  (placeholder as HTMLElement).style.display = 'flex';
                }
              }}
            />
          )}
          <div className={styles.imagePlaceholder} style={{ display: image ? 'none' : 'flex' }}>
            <span className={styles.placeholderIcon}>📚</span>
          </div>
        </div>
        <div className={styles.cardContent}>
          <h3 className={styles.cardTitle}>{title}</h3>
          <p className={styles.cardDescription}>{description}</p>
        </div>
      </a>
    </div>
  );
}

export default function HomepageFeatures() {
  return (
    <section className={styles.features}>
      <div className={styles.container}>
        <h2 className={styles.sectionTitle}>Explore the Book Modules</h2>
        <p className={styles.sectionSubtitle}>
          Dive deep into each topic and build your expertise in Physical AI and Humanoid Robotics
        </p>
        <div className={styles.moduleGrid}>
          {ModuleList.map((props, idx) => (
            <ModuleCard key={idx} {...props} />
          ))}
        </div>
      </div>
    </section>
  );
}
