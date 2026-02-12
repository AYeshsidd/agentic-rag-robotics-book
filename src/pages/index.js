import React from 'react';
import clsx from 'clsx';
import Layout from '@theme/Layout';
import Link from '@docusaurus/Link';
import useDocusaurusContext from '@docusaurus/useDocusaurusContext';
import styles from './index.module.css';
import HomepageFeatures from '@site/src/components/HomepageFeatures';

function HomepageHeader() {
  const {siteConfig} = useDocusaurusContext();
  return (
    <header className={clsx('hero', styles.heroBanner)}>
      <div className={styles.heroContent}>
        <h1 className={styles.heroTitle}>
          <span className={styles.heroTitleGradient}>{siteConfig.title}</span>
        </h1>
        <p className={styles.heroSubtitle}>{siteConfig.tagline}</p>
        <div className={styles.buttons}>
          <Link
            className={clsx('button button--lg', styles.heroButton)}
            to="/docs/ros2-nervous-system/chapter1">
            🤖 Open Physical AI Book
          </Link>
        </div>
        <div className={styles.chatbotHint}>
          <span className={styles.hintIcon}></span>
          <p>Click the AI assistant (⚙️) in the bottom-right to get instant explanations from the book</p>
        </div>
      </div>
    </header>
  );
}

export default function Home() {
  const {siteConfig} = useDocusaurusContext();
  return (
    <Layout
      title={`Welcome | ${siteConfig.title}`}
      description="Description will go into a meta tag in <head />">
      <HomepageHeader />
      <main>
        <HomepageFeatures />
      </main>
    </Layout>
  );
}
