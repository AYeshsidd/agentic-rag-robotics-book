import React from 'react';
import FloatingChatbot from '@site/src/components/FloatingChatbot';

export default function Root({ children }) {
  return (
    <>
      {children}
      <FloatingChatbot />
    </>
  );
}
