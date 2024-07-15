# TailorMade

TailorMade is an innovative tool designed to personalize clothing and makeup products based on individual body type and color palette analysis. It aims to provide users with tailored recommendations that enhance their natural features and fit their unique profiles.

## Features

TailorMade consists of two main components:

1. **Body Type Analysis**:
    - Input measurements: bust size, waist size, hip size, and lower hip size.
    - Determines the user's body shape category (e.g., Apple, Banana, Pear, Hourglass).
    - Provides personalized clothing recommendations based on the body shape.

2. **Color Palette Analysis**:
    - Inputs: skin tone, eye color, and hair color.
    - Generates a personalized color palette for clothing and makeup.
    - Helps users choose colors that complement their natural features.

## How It Works

### Body Type Analysis

To determine the user's body shape, TailorMade takes the following measurements:
- **Bust size**: The circumference measured around the chest over the fullest part of the breasts.
- **Waist size**: The smallest circumference measured around the natural waist, just above the belly button.
- **Hip size**: The largest circumference measured around the hips over the largest part of the buttocks.
- **Lower hip size**: The circumference of the upper swell of the hip over the pelvic region, around 7 inches (18 cm) below the natural waist.

Based on these measurements, the tool classifies the body shape into one of the following categories:
- **Apple (Inverted Triangle)**: Broader shoulders and bust than hips.
- **Banana (Rectangle)**: Waist measurements are less than 9 inches smaller than the hip or bust measurements.
- **Pear (Triangle)**: Hip measurements are greater than bust measurements.
- **Hourglass (X shape)**: Hip and bust measurements are nearly equal, with a narrower waist.

### Color Palette Analysis

TailorMade analyzes the user's skin tone, eye color, and hair color to generate a personalized color palette. This palette includes colors that are most flattering for the user's unique features and can be used for both clothing and makeup recommendations.

## Machine Learning for Product Recommendations

TailorMade uses machine learning algorithms to suggest products that best fit the user's profile. The suggested algorithm for this purpose is the **Collaborative Filtering Algorithm**.

### Collaborative Filtering Algorithm

This algorithm is widely used in recommendation systems. It works by finding patterns in user behavior and preferences to suggest products that similar users have liked. Here's how it can be applied in TailorMade:
- **User-Based Collaborative Filtering**: Recommends products based on similarities between users' profiles and preferences.
- **Item-Based Collaborative Filtering**: Recommends products based on similarities between items that users with similar profiles have liked.

By combining body type and color palette data, the algorithm can provide highly personalized recommendations for clothing and makeup products.
