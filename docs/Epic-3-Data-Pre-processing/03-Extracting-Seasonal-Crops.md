# Extracting Seasonal Crops

## Overview

Seasonal crop extraction is performed to identify crops that are best suited for different environmental conditions based on temperature, humidity, and rainfall. In the **OptiCrop: Smart Agricultural Production Optimization Engine**, agricultural data is filtered using predefined climatic conditions to group crops into **summer**, **winter**, and **rainy** seasons.

This analysis helps farmers select suitable crops according to seasonal weather conditions, improving crop productivity and supporting intelligent agricultural decision-making.

---

## Objective

The objectives of this step are to:

- Classify crops based on seasonal environmental conditions.
- Identify crops suitable for summer, winter, and rainy seasons.
- Analyze the influence of temperature, humidity, and rainfall on crop selection.
- Support intelligent crop recommendation.
- Improve agricultural planning and decision-making.

---

## Python Code

```python
# Summer crops
print("Summer crops")
print(data[(data['temperature'] > 30) &
           (data['humidity'] > 50)]['label'].unique())

print("----------------------------------------------")

# Winter crops
print("Winter crops")
print(data[(data['temperature'] < 20) &
           (data['humidity'] > 30)]['label'].unique())

print("----------------------------------------------")

# Rainy season crops
print("Rainy crops")
print(data[(data['rainfall'] > 200) &
           (data['humidity'] > 50)]['label'].unique())

print("----------------------------------------------")
```

---

## Seasonal Criteria

The crops are extracted using the following environmental conditions:

| Season | Criteria |
|----------|----------|
| **Summer** | Temperature > 30°C and Humidity > 50% |
| **Winter** | Temperature < 20°C and Humidity > 30% |
| **Rainy** | Rainfall > 200 mm and Humidity > 50% |

---

## Sample Output

### Summer Crops

- Pigeonpeas
- Mothbeans
- Blackgram
- Mango
- Grapes
- Orange
- Papaya

### Winter Crops

- Maize
- Pigeonpeas
- Lentil
- Pomegranate
- Grapes
- Orange

### Rainy Season Crops

- Rice
- Papaya
- Coconut

---

## Observations

The seasonal crop analysis reveals the following:

- Crops are successfully grouped according to climatic conditions.
- Summer crops generally require higher temperatures and humidity.
- Winter crops are suitable for cooler temperatures with moderate humidity.
- Rainy season crops require high rainfall and humidity for optimal growth.
- Some crops appear in multiple seasonal groups because they can grow under a wider range of environmental conditions.

---

## Purpose

Extracting seasonal crops helps to:

- Recommend crops based on seasonal weather conditions.
- Improve crop selection accuracy.
- Support precision agriculture.
- Reduce the risk of crop failure.
- Enhance agricultural productivity through climate-based recommendations.

---

## Expected Outcome

After completing this step:

- Crops are categorized into summer, winter, and rainy seasons.
- Seasonal crop recommendations are generated.
- Environmental conditions influencing crop growth are identified.
- The system provides better support for intelligent crop recommendation.

---

## Conclusion

Extracting seasonal crops enables the **OptiCrop: Smart Agricultural Production Optimization Engine** to recommend crops based on climatic conditions such as temperature, humidity, and rainfall. This seasonal analysis supports data-driven agricultural planning, improves crop selection, enhances farming productivity, and promotes sustainable agricultural practices.
