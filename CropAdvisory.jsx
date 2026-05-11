// src/pages/CropAdvisory/CropAdvisory.jsx
import React from 'react';
import Weather from '../Weather/Weather';
import Fertilizer from '../Fertilizer/Fertilizer';
import CropRecommend from '../CropRecommend/CropRecommend';
import { theme } from '../../styles/theme';

const CropAdvisory = () => {
  return (
    <div style={{ display: 'flex', flexDirection: 'column', gap: 24 }}>

      {/* ── Row 1: Weather + Fertilizer (your existing layout) ── */}
      <div style={{
        display: 'grid',
        gridTemplateColumns: '1fr 1fr',
        gap: 20,
        alignItems: 'stretch',
        gridAutoRows: '1fr',
      }}>
        <div style={{ height: '100%' }}><Weather /></div>
        <div style={{ height: '100%' }}><Fertilizer /></div>
      </div>

      {/* ── Row 2: AI Crop Recommendation (full width) ── */}
      <CropRecommend />

    </div>
  );
};

export default CropAdvisory;
