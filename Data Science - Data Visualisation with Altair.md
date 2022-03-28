# <h1><center>Data Science - Data Visualisation with Altair</center></h1>


```python
# • Go to: https://www.kaggle.com/datasets 

# • Select a dataset

# • Then create a data dashboard using Altair or Tableau  https://public.tableau.com/en-us/s/ 

# • Then create a markdown cell explain why you have decided on the design choices, what influenced your decisions and what 
# insights have you found from the data.
```


```python
import altair as alt
import pandas as pd
import numpy as np
```


```python
dataset = pd.read_csv (r'C:\Users\sudip\holiday_destination.csv')
print (dataset)
```

       holiday_destination most_visited_city      country  all_inclusive_package  \
    0         Burj Khalifa             Dubai          UAE                     20   
    1            MGM Grand         Las Vegas          USA                     15   
    2         Tower Bridge            London           UK                      9   
    3        Tokyo Skytree             Tokyo        Japan                     16   
    4        Palolem Beach               Goa        India                     21   
    5            Khao Rang            Phuket     Thailand                     12   
    6          Mount Batur              Bali    Indonesia                      7   
    7    Escadaria Selarón    Rio de Janeiro       Brazil                     25   
    8      Grouse Mountain         Vancouver       Canada                     18   
    9           Lovrijenac         Dubrovnik      Croatia                      8   
    10           Red Beach         Santorini       Greece                     19   
    11    Düden Waterfalls           Antalya       Turkey                     15   
    12           Colosseum              Rome        Italy                     17   
    13         Opera House            Sydney    Australia                     10   
    14          Vondelpark         Amsterdam  Netherlands                      6   
    
       feedback_score  hotel_star_rating  average_review_score  
    0       Excellent                4.7                   9.6  
    1       Very Good                4.0                   8.9  
    2       Excellent                4.7                   8.6  
    3       Very Good                4.4                   8.4  
    4       Excellent                4.6                   8.2  
    5       Very Good                4.5                   7.3  
    6       Excellent                4.6                   8.2  
    7       Excellent                4.6                   8.2  
    8       Excellent                4.5                   7.5  
    9       Excellent                4.7                   8.6  
    10      Very Good                4.1                   6.9  
    11      Excellent                4.7                   8.3  
    12      Excellent                4.7                   7.5  
    13      Excellent                4.7                   9.3  
    14      Excellent                4.7                   8.3  
    


```python
# Size of Dataset
```


```python
print(dataset.shape)
```

    (15, 7)
    


```python
# Top 5 Rows
```


```python
dataset.head(5)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>holiday_destination</th>
      <th>most_visited_city</th>
      <th>country</th>
      <th>all_inclusive_package</th>
      <th>feedback_score</th>
      <th>hotel_star_rating</th>
      <th>average_review_score</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Burj Khalifa</td>
      <td>Dubai</td>
      <td>UAE</td>
      <td>20</td>
      <td>Excellent</td>
      <td>4.7</td>
      <td>9.6</td>
    </tr>
    <tr>
      <th>1</th>
      <td>MGM Grand</td>
      <td>Las Vegas</td>
      <td>USA</td>
      <td>15</td>
      <td>Very Good</td>
      <td>4.0</td>
      <td>8.9</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Tower Bridge</td>
      <td>London</td>
      <td>UK</td>
      <td>9</td>
      <td>Excellent</td>
      <td>4.7</td>
      <td>8.6</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Tokyo Skytree</td>
      <td>Tokyo</td>
      <td>Japan</td>
      <td>16</td>
      <td>Very Good</td>
      <td>4.4</td>
      <td>8.4</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Palolem Beach</td>
      <td>Goa</td>
      <td>India</td>
      <td>21</td>
      <td>Excellent</td>
      <td>4.6</td>
      <td>8.2</td>
    </tr>
  </tbody>
</table>
</div>




```python
# The statistical details of the dataset using describe().
```


```python
dataset.describe()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>all_inclusive_package</th>
      <th>hotel_star_rating</th>
      <th>average_review_score</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>15.000000</td>
      <td>15.000000</td>
      <td>15.000000</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>14.533333</td>
      <td>4.546667</td>
      <td>8.253333</td>
    </tr>
    <tr>
      <th>std</th>
      <td>5.680376</td>
      <td>0.223180</td>
      <td>0.730818</td>
    </tr>
    <tr>
      <th>min</th>
      <td>6.000000</td>
      <td>4.000000</td>
      <td>6.900000</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>9.500000</td>
      <td>4.500000</td>
      <td>7.850000</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>15.000000</td>
      <td>4.600000</td>
      <td>8.300000</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>18.500000</td>
      <td>4.700000</td>
      <td>8.600000</td>
    </tr>
    <tr>
      <th>max</th>
      <td>25.000000</td>
      <td>4.700000</td>
      <td>9.600000</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Plotting and Creating Charts
```


```python
alt.Chart(dataset).mark_point().encode(
    x='average_review_score', 
    y='most_visited_city',
    color='feedback_score'
).interactive()
```





<div id="altair-viz-0c46644e6ca6427f81be26384219dc3f"></div>
<script type="text/javascript">
  var VEGA_DEBUG = (typeof VEGA_DEBUG == "undefined") ? {} : VEGA_DEBUG;
  (function(spec, embedOpt){
    let outputDiv = document.currentScript.previousElementSibling;
    if (outputDiv.id !== "altair-viz-0c46644e6ca6427f81be26384219dc3f") {
      outputDiv = document.getElementById("altair-viz-0c46644e6ca6427f81be26384219dc3f");
    }
    const paths = {
      "vega": "https://cdn.jsdelivr.net/npm//vega@5?noext",
      "vega-lib": "https://cdn.jsdelivr.net/npm//vega-lib?noext",
      "vega-lite": "https://cdn.jsdelivr.net/npm//vega-lite@4.17.0?noext",
      "vega-embed": "https://cdn.jsdelivr.net/npm//vega-embed@6?noext",
    };

    function maybeLoadScript(lib, version) {
      var key = `${lib.replace("-", "")}_version`;
      return (VEGA_DEBUG[key] == version) ?
        Promise.resolve(paths[lib]) :
        new Promise(function(resolve, reject) {
          var s = document.createElement('script');
          document.getElementsByTagName("head")[0].appendChild(s);
          s.async = true;
          s.onload = () => {
            VEGA_DEBUG[key] = version;
            return resolve(paths[lib]);
          };
          s.onerror = () => reject(`Error loading script: ${paths[lib]}`);
          s.src = paths[lib];
        });
    }

    function showError(err) {
      outputDiv.innerHTML = `<div class="error" style="color:red;">${err}</div>`;
      throw err;
    }

    function displayChart(vegaEmbed) {
      vegaEmbed(outputDiv, spec, embedOpt)
        .catch(err => showError(`Javascript Error: ${err.message}<br>This usually means there's a typo in your chart specification. See the javascript console for the full traceback.`));
    }

    if(typeof define === "function" && define.amd) {
      requirejs.config({paths});
      require(["vega-embed"], displayChart, err => showError(`Error loading script: ${err.message}`));
    } else {
      maybeLoadScript("vega", "5")
        .then(() => maybeLoadScript("vega-lite", "4.17.0"))
        .then(() => maybeLoadScript("vega-embed", "6"))
        .catch(showError)
        .then(() => displayChart(vegaEmbed));
    }
  })({"config": {"view": {"continuousWidth": 400, "continuousHeight": 300}}, "data": {"name": "data-dd9fd859cdad3a09d77f58896ce38134"}, "mark": "point", "encoding": {"color": {"field": "feedback_score", "type": "nominal"}, "x": {"field": "average_review_score", "type": "quantitative"}, "y": {"field": "most_visited_city", "type": "nominal"}}, "selection": {"selector001": {"type": "interval", "bind": "scales", "encodings": ["x", "y"]}}, "$schema": "https://vega.github.io/schema/vega-lite/v4.17.0.json", "datasets": {"data-dd9fd859cdad3a09d77f58896ce38134": [{"holiday_destination": "Burj Khalifa", "most_visited_city": "Dubai", "country": "UAE", "all_inclusive_package": 20, "feedback_score": "Excellent", "hotel_star_rating": 4.7, "average_review_score": 9.6}, {"holiday_destination": "MGM Grand", "most_visited_city": "Las Vegas", "country": "USA", "all_inclusive_package": 15, "feedback_score": "Very Good", "hotel_star_rating": 4.0, "average_review_score": 8.9}, {"holiday_destination": "Tower Bridge", "most_visited_city": "London", "country": "UK", "all_inclusive_package": 9, "feedback_score": "Excellent", "hotel_star_rating": 4.7, "average_review_score": 8.6}, {"holiday_destination": "Tokyo Skytree", "most_visited_city": "Tokyo", "country": "Japan", "all_inclusive_package": 16, "feedback_score": "Very Good", "hotel_star_rating": 4.4, "average_review_score": 8.4}, {"holiday_destination": "Palolem Beach", "most_visited_city": "Goa", "country": "India", "all_inclusive_package": 21, "feedback_score": "Excellent", "hotel_star_rating": 4.6, "average_review_score": 8.2}, {"holiday_destination": "Khao Rang", "most_visited_city": "Phuket", "country": "Thailand", "all_inclusive_package": 12, "feedback_score": "Very Good", "hotel_star_rating": 4.5, "average_review_score": 7.3}, {"holiday_destination": "Mount Batur", "most_visited_city": "Bali", "country": "Indonesia", "all_inclusive_package": 7, "feedback_score": "Excellent", "hotel_star_rating": 4.6, "average_review_score": 8.2}, {"holiday_destination": "Escadaria Selar\u00f3n", "most_visited_city": "Rio de Janeiro", "country": "Brazil", "all_inclusive_package": 25, "feedback_score": "Excellent", "hotel_star_rating": 4.6, "average_review_score": 8.2}, {"holiday_destination": "Grouse Mountain", "most_visited_city": "Vancouver", "country": "Canada", "all_inclusive_package": 18, "feedback_score": "Excellent", "hotel_star_rating": 4.5, "average_review_score": 7.5}, {"holiday_destination": "Lovrijenac", "most_visited_city": "Dubrovnik", "country": "Croatia", "all_inclusive_package": 8, "feedback_score": "Excellent", "hotel_star_rating": 4.7, "average_review_score": 8.6}, {"holiday_destination": "Red Beach", "most_visited_city": "Santorini", "country": "Greece", "all_inclusive_package": 19, "feedback_score": "Very Good", "hotel_star_rating": 4.1, "average_review_score": 6.9}, {"holiday_destination": "D\u00fcden Waterfalls", "most_visited_city": "Antalya", "country": "Turkey", "all_inclusive_package": 15, "feedback_score": "Excellent", "hotel_star_rating": 4.7, "average_review_score": 8.3}, {"holiday_destination": "Colosseum", "most_visited_city": "Rome", "country": "Italy", "all_inclusive_package": 17, "feedback_score": "Excellent", "hotel_star_rating": 4.7, "average_review_score": 7.5}, {"holiday_destination": "Opera House", "most_visited_city": "Sydney", "country": "Australia", "all_inclusive_package": 10, "feedback_score": "Excellent", "hotel_star_rating": 4.7, "average_review_score": 9.3}, {"holiday_destination": "Vondelpark", "most_visited_city": "Amsterdam", "country": "Netherlands", "all_inclusive_package": 6, "feedback_score": "Excellent", "hotel_star_rating": 4.7, "average_review_score": 8.3}]}}, {"mode": "vega-lite"});
</script>




```python
alt.Chart(dataset).mark_point().encode(
    x='average_review_score', 
    y='holiday_destination',
    color='most_visited_city'
).interactive()
```





<div id="altair-viz-91b374616dab437fb8e3056da96c4808"></div>
<script type="text/javascript">
  var VEGA_DEBUG = (typeof VEGA_DEBUG == "undefined") ? {} : VEGA_DEBUG;
  (function(spec, embedOpt){
    let outputDiv = document.currentScript.previousElementSibling;
    if (outputDiv.id !== "altair-viz-91b374616dab437fb8e3056da96c4808") {
      outputDiv = document.getElementById("altair-viz-91b374616dab437fb8e3056da96c4808");
    }
    const paths = {
      "vega": "https://cdn.jsdelivr.net/npm//vega@5?noext",
      "vega-lib": "https://cdn.jsdelivr.net/npm//vega-lib?noext",
      "vega-lite": "https://cdn.jsdelivr.net/npm//vega-lite@4.17.0?noext",
      "vega-embed": "https://cdn.jsdelivr.net/npm//vega-embed@6?noext",
    };

    function maybeLoadScript(lib, version) {
      var key = `${lib.replace("-", "")}_version`;
      return (VEGA_DEBUG[key] == version) ?
        Promise.resolve(paths[lib]) :
        new Promise(function(resolve, reject) {
          var s = document.createElement('script');
          document.getElementsByTagName("head")[0].appendChild(s);
          s.async = true;
          s.onload = () => {
            VEGA_DEBUG[key] = version;
            return resolve(paths[lib]);
          };
          s.onerror = () => reject(`Error loading script: ${paths[lib]}`);
          s.src = paths[lib];
        });
    }

    function showError(err) {
      outputDiv.innerHTML = `<div class="error" style="color:red;">${err}</div>`;
      throw err;
    }

    function displayChart(vegaEmbed) {
      vegaEmbed(outputDiv, spec, embedOpt)
        .catch(err => showError(`Javascript Error: ${err.message}<br>This usually means there's a typo in your chart specification. See the javascript console for the full traceback.`));
    }

    if(typeof define === "function" && define.amd) {
      requirejs.config({paths});
      require(["vega-embed"], displayChart, err => showError(`Error loading script: ${err.message}`));
    } else {
      maybeLoadScript("vega", "5")
        .then(() => maybeLoadScript("vega-lite", "4.17.0"))
        .then(() => maybeLoadScript("vega-embed", "6"))
        .catch(showError)
        .then(() => displayChart(vegaEmbed));
    }
  })({"config": {"view": {"continuousWidth": 400, "continuousHeight": 300}}, "data": {"name": "data-dd9fd859cdad3a09d77f58896ce38134"}, "mark": "point", "encoding": {"color": {"field": "most_visited_city", "type": "nominal"}, "x": {"field": "average_review_score", "type": "quantitative"}, "y": {"field": "holiday_destination", "type": "nominal"}}, "selection": {"selector002": {"type": "interval", "bind": "scales", "encodings": ["x", "y"]}}, "$schema": "https://vega.github.io/schema/vega-lite/v4.17.0.json", "datasets": {"data-dd9fd859cdad3a09d77f58896ce38134": [{"holiday_destination": "Burj Khalifa", "most_visited_city": "Dubai", "country": "UAE", "all_inclusive_package": 20, "feedback_score": "Excellent", "hotel_star_rating": 4.7, "average_review_score": 9.6}, {"holiday_destination": "MGM Grand", "most_visited_city": "Las Vegas", "country": "USA", "all_inclusive_package": 15, "feedback_score": "Very Good", "hotel_star_rating": 4.0, "average_review_score": 8.9}, {"holiday_destination": "Tower Bridge", "most_visited_city": "London", "country": "UK", "all_inclusive_package": 9, "feedback_score": "Excellent", "hotel_star_rating": 4.7, "average_review_score": 8.6}, {"holiday_destination": "Tokyo Skytree", "most_visited_city": "Tokyo", "country": "Japan", "all_inclusive_package": 16, "feedback_score": "Very Good", "hotel_star_rating": 4.4, "average_review_score": 8.4}, {"holiday_destination": "Palolem Beach", "most_visited_city": "Goa", "country": "India", "all_inclusive_package": 21, "feedback_score": "Excellent", "hotel_star_rating": 4.6, "average_review_score": 8.2}, {"holiday_destination": "Khao Rang", "most_visited_city": "Phuket", "country": "Thailand", "all_inclusive_package": 12, "feedback_score": "Very Good", "hotel_star_rating": 4.5, "average_review_score": 7.3}, {"holiday_destination": "Mount Batur", "most_visited_city": "Bali", "country": "Indonesia", "all_inclusive_package": 7, "feedback_score": "Excellent", "hotel_star_rating": 4.6, "average_review_score": 8.2}, {"holiday_destination": "Escadaria Selar\u00f3n", "most_visited_city": "Rio de Janeiro", "country": "Brazil", "all_inclusive_package": 25, "feedback_score": "Excellent", "hotel_star_rating": 4.6, "average_review_score": 8.2}, {"holiday_destination": "Grouse Mountain", "most_visited_city": "Vancouver", "country": "Canada", "all_inclusive_package": 18, "feedback_score": "Excellent", "hotel_star_rating": 4.5, "average_review_score": 7.5}, {"holiday_destination": "Lovrijenac", "most_visited_city": "Dubrovnik", "country": "Croatia", "all_inclusive_package": 8, "feedback_score": "Excellent", "hotel_star_rating": 4.7, "average_review_score": 8.6}, {"holiday_destination": "Red Beach", "most_visited_city": "Santorini", "country": "Greece", "all_inclusive_package": 19, "feedback_score": "Very Good", "hotel_star_rating": 4.1, "average_review_score": 6.9}, {"holiday_destination": "D\u00fcden Waterfalls", "most_visited_city": "Antalya", "country": "Turkey", "all_inclusive_package": 15, "feedback_score": "Excellent", "hotel_star_rating": 4.7, "average_review_score": 8.3}, {"holiday_destination": "Colosseum", "most_visited_city": "Rome", "country": "Italy", "all_inclusive_package": 17, "feedback_score": "Excellent", "hotel_star_rating": 4.7, "average_review_score": 7.5}, {"holiday_destination": "Opera House", "most_visited_city": "Sydney", "country": "Australia", "all_inclusive_package": 10, "feedback_score": "Excellent", "hotel_star_rating": 4.7, "average_review_score": 9.3}, {"holiday_destination": "Vondelpark", "most_visited_city": "Amsterdam", "country": "Netherlands", "all_inclusive_package": 6, "feedback_score": "Excellent", "hotel_star_rating": 4.7, "average_review_score": 8.3}]}}, {"mode": "vega-lite"});
</script>




```python
alt.Chart(dataset).mark_point().encode(
    x='average_review_score', 
    y='holiday_destination',
    size='hotel_star_rating',
).interactive()
```





<div id="altair-viz-f4d86709e20d4ef19d715ffefdded4ea"></div>
<script type="text/javascript">
  var VEGA_DEBUG = (typeof VEGA_DEBUG == "undefined") ? {} : VEGA_DEBUG;
  (function(spec, embedOpt){
    let outputDiv = document.currentScript.previousElementSibling;
    if (outputDiv.id !== "altair-viz-f4d86709e20d4ef19d715ffefdded4ea") {
      outputDiv = document.getElementById("altair-viz-f4d86709e20d4ef19d715ffefdded4ea");
    }
    const paths = {
      "vega": "https://cdn.jsdelivr.net/npm//vega@5?noext",
      "vega-lib": "https://cdn.jsdelivr.net/npm//vega-lib?noext",
      "vega-lite": "https://cdn.jsdelivr.net/npm//vega-lite@4.17.0?noext",
      "vega-embed": "https://cdn.jsdelivr.net/npm//vega-embed@6?noext",
    };

    function maybeLoadScript(lib, version) {
      var key = `${lib.replace("-", "")}_version`;
      return (VEGA_DEBUG[key] == version) ?
        Promise.resolve(paths[lib]) :
        new Promise(function(resolve, reject) {
          var s = document.createElement('script');
          document.getElementsByTagName("head")[0].appendChild(s);
          s.async = true;
          s.onload = () => {
            VEGA_DEBUG[key] = version;
            return resolve(paths[lib]);
          };
          s.onerror = () => reject(`Error loading script: ${paths[lib]}`);
          s.src = paths[lib];
        });
    }

    function showError(err) {
      outputDiv.innerHTML = `<div class="error" style="color:red;">${err}</div>`;
      throw err;
    }

    function displayChart(vegaEmbed) {
      vegaEmbed(outputDiv, spec, embedOpt)
        .catch(err => showError(`Javascript Error: ${err.message}<br>This usually means there's a typo in your chart specification. See the javascript console for the full traceback.`));
    }

    if(typeof define === "function" && define.amd) {
      requirejs.config({paths});
      require(["vega-embed"], displayChart, err => showError(`Error loading script: ${err.message}`));
    } else {
      maybeLoadScript("vega", "5")
        .then(() => maybeLoadScript("vega-lite", "4.17.0"))
        .then(() => maybeLoadScript("vega-embed", "6"))
        .catch(showError)
        .then(() => displayChart(vegaEmbed));
    }
  })({"config": {"view": {"continuousWidth": 400, "continuousHeight": 300}}, "data": {"name": "data-dd9fd859cdad3a09d77f58896ce38134"}, "mark": "point", "encoding": {"size": {"field": "hotel_star_rating", "type": "quantitative"}, "x": {"field": "average_review_score", "type": "quantitative"}, "y": {"field": "holiday_destination", "type": "nominal"}}, "selection": {"selector003": {"type": "interval", "bind": "scales", "encodings": ["x", "y"]}}, "$schema": "https://vega.github.io/schema/vega-lite/v4.17.0.json", "datasets": {"data-dd9fd859cdad3a09d77f58896ce38134": [{"holiday_destination": "Burj Khalifa", "most_visited_city": "Dubai", "country": "UAE", "all_inclusive_package": 20, "feedback_score": "Excellent", "hotel_star_rating": 4.7, "average_review_score": 9.6}, {"holiday_destination": "MGM Grand", "most_visited_city": "Las Vegas", "country": "USA", "all_inclusive_package": 15, "feedback_score": "Very Good", "hotel_star_rating": 4.0, "average_review_score": 8.9}, {"holiday_destination": "Tower Bridge", "most_visited_city": "London", "country": "UK", "all_inclusive_package": 9, "feedback_score": "Excellent", "hotel_star_rating": 4.7, "average_review_score": 8.6}, {"holiday_destination": "Tokyo Skytree", "most_visited_city": "Tokyo", "country": "Japan", "all_inclusive_package": 16, "feedback_score": "Very Good", "hotel_star_rating": 4.4, "average_review_score": 8.4}, {"holiday_destination": "Palolem Beach", "most_visited_city": "Goa", "country": "India", "all_inclusive_package": 21, "feedback_score": "Excellent", "hotel_star_rating": 4.6, "average_review_score": 8.2}, {"holiday_destination": "Khao Rang", "most_visited_city": "Phuket", "country": "Thailand", "all_inclusive_package": 12, "feedback_score": "Very Good", "hotel_star_rating": 4.5, "average_review_score": 7.3}, {"holiday_destination": "Mount Batur", "most_visited_city": "Bali", "country": "Indonesia", "all_inclusive_package": 7, "feedback_score": "Excellent", "hotel_star_rating": 4.6, "average_review_score": 8.2}, {"holiday_destination": "Escadaria Selar\u00f3n", "most_visited_city": "Rio de Janeiro", "country": "Brazil", "all_inclusive_package": 25, "feedback_score": "Excellent", "hotel_star_rating": 4.6, "average_review_score": 8.2}, {"holiday_destination": "Grouse Mountain", "most_visited_city": "Vancouver", "country": "Canada", "all_inclusive_package": 18, "feedback_score": "Excellent", "hotel_star_rating": 4.5, "average_review_score": 7.5}, {"holiday_destination": "Lovrijenac", "most_visited_city": "Dubrovnik", "country": "Croatia", "all_inclusive_package": 8, "feedback_score": "Excellent", "hotel_star_rating": 4.7, "average_review_score": 8.6}, {"holiday_destination": "Red Beach", "most_visited_city": "Santorini", "country": "Greece", "all_inclusive_package": 19, "feedback_score": "Very Good", "hotel_star_rating": 4.1, "average_review_score": 6.9}, {"holiday_destination": "D\u00fcden Waterfalls", "most_visited_city": "Antalya", "country": "Turkey", "all_inclusive_package": 15, "feedback_score": "Excellent", "hotel_star_rating": 4.7, "average_review_score": 8.3}, {"holiday_destination": "Colosseum", "most_visited_city": "Rome", "country": "Italy", "all_inclusive_package": 17, "feedback_score": "Excellent", "hotel_star_rating": 4.7, "average_review_score": 7.5}, {"holiday_destination": "Opera House", "most_visited_city": "Sydney", "country": "Australia", "all_inclusive_package": 10, "feedback_score": "Excellent", "hotel_star_rating": 4.7, "average_review_score": 9.3}, {"holiday_destination": "Vondelpark", "most_visited_city": "Amsterdam", "country": "Netherlands", "all_inclusive_package": 6, "feedback_score": "Excellent", "hotel_star_rating": 4.7, "average_review_score": 8.3}]}}, {"mode": "vega-lite"});
</script>




```python
barPlot = alt.Chart(dataset).mark_bar().encode(
    x='all_inclusive_package', 
    y='holiday_destination',
    size ='hotel_star_rating',
    color='hotel_star_rating:N'
).interactive()
barPlot
```





<div id="altair-viz-8904acf8626d456f92898d79246808d0"></div>
<script type="text/javascript">
  var VEGA_DEBUG = (typeof VEGA_DEBUG == "undefined") ? {} : VEGA_DEBUG;
  (function(spec, embedOpt){
    let outputDiv = document.currentScript.previousElementSibling;
    if (outputDiv.id !== "altair-viz-8904acf8626d456f92898d79246808d0") {
      outputDiv = document.getElementById("altair-viz-8904acf8626d456f92898d79246808d0");
    }
    const paths = {
      "vega": "https://cdn.jsdelivr.net/npm//vega@5?noext",
      "vega-lib": "https://cdn.jsdelivr.net/npm//vega-lib?noext",
      "vega-lite": "https://cdn.jsdelivr.net/npm//vega-lite@4.17.0?noext",
      "vega-embed": "https://cdn.jsdelivr.net/npm//vega-embed@6?noext",
    };

    function maybeLoadScript(lib, version) {
      var key = `${lib.replace("-", "")}_version`;
      return (VEGA_DEBUG[key] == version) ?
        Promise.resolve(paths[lib]) :
        new Promise(function(resolve, reject) {
          var s = document.createElement('script');
          document.getElementsByTagName("head")[0].appendChild(s);
          s.async = true;
          s.onload = () => {
            VEGA_DEBUG[key] = version;
            return resolve(paths[lib]);
          };
          s.onerror = () => reject(`Error loading script: ${paths[lib]}`);
          s.src = paths[lib];
        });
    }

    function showError(err) {
      outputDiv.innerHTML = `<div class="error" style="color:red;">${err}</div>`;
      throw err;
    }

    function displayChart(vegaEmbed) {
      vegaEmbed(outputDiv, spec, embedOpt)
        .catch(err => showError(`Javascript Error: ${err.message}<br>This usually means there's a typo in your chart specification. See the javascript console for the full traceback.`));
    }

    if(typeof define === "function" && define.amd) {
      requirejs.config({paths});
      require(["vega-embed"], displayChart, err => showError(`Error loading script: ${err.message}`));
    } else {
      maybeLoadScript("vega", "5")
        .then(() => maybeLoadScript("vega-lite", "4.17.0"))
        .then(() => maybeLoadScript("vega-embed", "6"))
        .catch(showError)
        .then(() => displayChart(vegaEmbed));
    }
  })({"config": {"view": {"continuousWidth": 400, "continuousHeight": 300}}, "data": {"name": "data-dd9fd859cdad3a09d77f58896ce38134"}, "mark": "bar", "encoding": {"color": {"field": "hotel_star_rating", "type": "nominal"}, "size": {"field": "hotel_star_rating", "type": "quantitative"}, "x": {"field": "all_inclusive_package", "type": "quantitative"}, "y": {"field": "holiday_destination", "type": "nominal"}}, "selection": {"selector004": {"type": "interval", "bind": "scales", "encodings": ["x", "y"]}}, "$schema": "https://vega.github.io/schema/vega-lite/v4.17.0.json", "datasets": {"data-dd9fd859cdad3a09d77f58896ce38134": [{"holiday_destination": "Burj Khalifa", "most_visited_city": "Dubai", "country": "UAE", "all_inclusive_package": 20, "feedback_score": "Excellent", "hotel_star_rating": 4.7, "average_review_score": 9.6}, {"holiday_destination": "MGM Grand", "most_visited_city": "Las Vegas", "country": "USA", "all_inclusive_package": 15, "feedback_score": "Very Good", "hotel_star_rating": 4.0, "average_review_score": 8.9}, {"holiday_destination": "Tower Bridge", "most_visited_city": "London", "country": "UK", "all_inclusive_package": 9, "feedback_score": "Excellent", "hotel_star_rating": 4.7, "average_review_score": 8.6}, {"holiday_destination": "Tokyo Skytree", "most_visited_city": "Tokyo", "country": "Japan", "all_inclusive_package": 16, "feedback_score": "Very Good", "hotel_star_rating": 4.4, "average_review_score": 8.4}, {"holiday_destination": "Palolem Beach", "most_visited_city": "Goa", "country": "India", "all_inclusive_package": 21, "feedback_score": "Excellent", "hotel_star_rating": 4.6, "average_review_score": 8.2}, {"holiday_destination": "Khao Rang", "most_visited_city": "Phuket", "country": "Thailand", "all_inclusive_package": 12, "feedback_score": "Very Good", "hotel_star_rating": 4.5, "average_review_score": 7.3}, {"holiday_destination": "Mount Batur", "most_visited_city": "Bali", "country": "Indonesia", "all_inclusive_package": 7, "feedback_score": "Excellent", "hotel_star_rating": 4.6, "average_review_score": 8.2}, {"holiday_destination": "Escadaria Selar\u00f3n", "most_visited_city": "Rio de Janeiro", "country": "Brazil", "all_inclusive_package": 25, "feedback_score": "Excellent", "hotel_star_rating": 4.6, "average_review_score": 8.2}, {"holiday_destination": "Grouse Mountain", "most_visited_city": "Vancouver", "country": "Canada", "all_inclusive_package": 18, "feedback_score": "Excellent", "hotel_star_rating": 4.5, "average_review_score": 7.5}, {"holiday_destination": "Lovrijenac", "most_visited_city": "Dubrovnik", "country": "Croatia", "all_inclusive_package": 8, "feedback_score": "Excellent", "hotel_star_rating": 4.7, "average_review_score": 8.6}, {"holiday_destination": "Red Beach", "most_visited_city": "Santorini", "country": "Greece", "all_inclusive_package": 19, "feedback_score": "Very Good", "hotel_star_rating": 4.1, "average_review_score": 6.9}, {"holiday_destination": "D\u00fcden Waterfalls", "most_visited_city": "Antalya", "country": "Turkey", "all_inclusive_package": 15, "feedback_score": "Excellent", "hotel_star_rating": 4.7, "average_review_score": 8.3}, {"holiday_destination": "Colosseum", "most_visited_city": "Rome", "country": "Italy", "all_inclusive_package": 17, "feedback_score": "Excellent", "hotel_star_rating": 4.7, "average_review_score": 7.5}, {"holiday_destination": "Opera House", "most_visited_city": "Sydney", "country": "Australia", "all_inclusive_package": 10, "feedback_score": "Excellent", "hotel_star_rating": 4.7, "average_review_score": 9.3}, {"holiday_destination": "Vondelpark", "most_visited_city": "Amsterdam", "country": "Netherlands", "all_inclusive_package": 6, "feedback_score": "Excellent", "hotel_star_rating": 4.7, "average_review_score": 8.3}]}}, {"mode": "vega-lite"});
</script>




```python
circlePlot = alt.Chart(dataset).mark_circle().encode(
    x='all_inclusive_package', 
    y='holiday_destination',
    size = 'hotel_star_rating',
    color='hotel_star_rating:N',
    tooltip=['country','feedback_score'],
).interactive()
circlePlot
```





<div id="altair-viz-fc22564ec8b94ddc831b431d8d04ff8d"></div>
<script type="text/javascript">
  var VEGA_DEBUG = (typeof VEGA_DEBUG == "undefined") ? {} : VEGA_DEBUG;
  (function(spec, embedOpt){
    let outputDiv = document.currentScript.previousElementSibling;
    if (outputDiv.id !== "altair-viz-fc22564ec8b94ddc831b431d8d04ff8d") {
      outputDiv = document.getElementById("altair-viz-fc22564ec8b94ddc831b431d8d04ff8d");
    }
    const paths = {
      "vega": "https://cdn.jsdelivr.net/npm//vega@5?noext",
      "vega-lib": "https://cdn.jsdelivr.net/npm//vega-lib?noext",
      "vega-lite": "https://cdn.jsdelivr.net/npm//vega-lite@4.17.0?noext",
      "vega-embed": "https://cdn.jsdelivr.net/npm//vega-embed@6?noext",
    };

    function maybeLoadScript(lib, version) {
      var key = `${lib.replace("-", "")}_version`;
      return (VEGA_DEBUG[key] == version) ?
        Promise.resolve(paths[lib]) :
        new Promise(function(resolve, reject) {
          var s = document.createElement('script');
          document.getElementsByTagName("head")[0].appendChild(s);
          s.async = true;
          s.onload = () => {
            VEGA_DEBUG[key] = version;
            return resolve(paths[lib]);
          };
          s.onerror = () => reject(`Error loading script: ${paths[lib]}`);
          s.src = paths[lib];
        });
    }

    function showError(err) {
      outputDiv.innerHTML = `<div class="error" style="color:red;">${err}</div>`;
      throw err;
    }

    function displayChart(vegaEmbed) {
      vegaEmbed(outputDiv, spec, embedOpt)
        .catch(err => showError(`Javascript Error: ${err.message}<br>This usually means there's a typo in your chart specification. See the javascript console for the full traceback.`));
    }

    if(typeof define === "function" && define.amd) {
      requirejs.config({paths});
      require(["vega-embed"], displayChart, err => showError(`Error loading script: ${err.message}`));
    } else {
      maybeLoadScript("vega", "5")
        .then(() => maybeLoadScript("vega-lite", "4.17.0"))
        .then(() => maybeLoadScript("vega-embed", "6"))
        .catch(showError)
        .then(() => displayChart(vegaEmbed));
    }
  })({"config": {"view": {"continuousWidth": 400, "continuousHeight": 300}}, "data": {"name": "data-dd9fd859cdad3a09d77f58896ce38134"}, "mark": "circle", "encoding": {"color": {"field": "hotel_star_rating", "type": "nominal"}, "size": {"field": "hotel_star_rating", "type": "quantitative"}, "tooltip": [{"field": "country", "type": "nominal"}, {"field": "feedback_score", "type": "nominal"}], "x": {"field": "all_inclusive_package", "type": "quantitative"}, "y": {"field": "holiday_destination", "type": "nominal"}}, "selection": {"selector005": {"type": "interval", "bind": "scales", "encodings": ["x", "y"]}}, "$schema": "https://vega.github.io/schema/vega-lite/v4.17.0.json", "datasets": {"data-dd9fd859cdad3a09d77f58896ce38134": [{"holiday_destination": "Burj Khalifa", "most_visited_city": "Dubai", "country": "UAE", "all_inclusive_package": 20, "feedback_score": "Excellent", "hotel_star_rating": 4.7, "average_review_score": 9.6}, {"holiday_destination": "MGM Grand", "most_visited_city": "Las Vegas", "country": "USA", "all_inclusive_package": 15, "feedback_score": "Very Good", "hotel_star_rating": 4.0, "average_review_score": 8.9}, {"holiday_destination": "Tower Bridge", "most_visited_city": "London", "country": "UK", "all_inclusive_package": 9, "feedback_score": "Excellent", "hotel_star_rating": 4.7, "average_review_score": 8.6}, {"holiday_destination": "Tokyo Skytree", "most_visited_city": "Tokyo", "country": "Japan", "all_inclusive_package": 16, "feedback_score": "Very Good", "hotel_star_rating": 4.4, "average_review_score": 8.4}, {"holiday_destination": "Palolem Beach", "most_visited_city": "Goa", "country": "India", "all_inclusive_package": 21, "feedback_score": "Excellent", "hotel_star_rating": 4.6, "average_review_score": 8.2}, {"holiday_destination": "Khao Rang", "most_visited_city": "Phuket", "country": "Thailand", "all_inclusive_package": 12, "feedback_score": "Very Good", "hotel_star_rating": 4.5, "average_review_score": 7.3}, {"holiday_destination": "Mount Batur", "most_visited_city": "Bali", "country": "Indonesia", "all_inclusive_package": 7, "feedback_score": "Excellent", "hotel_star_rating": 4.6, "average_review_score": 8.2}, {"holiday_destination": "Escadaria Selar\u00f3n", "most_visited_city": "Rio de Janeiro", "country": "Brazil", "all_inclusive_package": 25, "feedback_score": "Excellent", "hotel_star_rating": 4.6, "average_review_score": 8.2}, {"holiday_destination": "Grouse Mountain", "most_visited_city": "Vancouver", "country": "Canada", "all_inclusive_package": 18, "feedback_score": "Excellent", "hotel_star_rating": 4.5, "average_review_score": 7.5}, {"holiday_destination": "Lovrijenac", "most_visited_city": "Dubrovnik", "country": "Croatia", "all_inclusive_package": 8, "feedback_score": "Excellent", "hotel_star_rating": 4.7, "average_review_score": 8.6}, {"holiday_destination": "Red Beach", "most_visited_city": "Santorini", "country": "Greece", "all_inclusive_package": 19, "feedback_score": "Very Good", "hotel_star_rating": 4.1, "average_review_score": 6.9}, {"holiday_destination": "D\u00fcden Waterfalls", "most_visited_city": "Antalya", "country": "Turkey", "all_inclusive_package": 15, "feedback_score": "Excellent", "hotel_star_rating": 4.7, "average_review_score": 8.3}, {"holiday_destination": "Colosseum", "most_visited_city": "Rome", "country": "Italy", "all_inclusive_package": 17, "feedback_score": "Excellent", "hotel_star_rating": 4.7, "average_review_score": 7.5}, {"holiday_destination": "Opera House", "most_visited_city": "Sydney", "country": "Australia", "all_inclusive_package": 10, "feedback_score": "Excellent", "hotel_star_rating": 4.7, "average_review_score": 9.3}, {"holiday_destination": "Vondelpark", "most_visited_city": "Amsterdam", "country": "Netherlands", "all_inclusive_package": 6, "feedback_score": "Excellent", "hotel_star_rating": 4.7, "average_review_score": 8.3}]}}, {"mode": "vega-lite"});
</script>




```python
stackbarPlot = alt.Chart(dataset).mark_bar().encode(
    x='average_review_score', 
    y='country',
    color='hotel_star_rating:N',
    tooltip=['holiday_destination', 'hotel_star_rating']

)
stackbarPlot
```





<div id="altair-viz-cf9eade10de9481fbc1f144b7c7910d2"></div>
<script type="text/javascript">
  var VEGA_DEBUG = (typeof VEGA_DEBUG == "undefined") ? {} : VEGA_DEBUG;
  (function(spec, embedOpt){
    let outputDiv = document.currentScript.previousElementSibling;
    if (outputDiv.id !== "altair-viz-cf9eade10de9481fbc1f144b7c7910d2") {
      outputDiv = document.getElementById("altair-viz-cf9eade10de9481fbc1f144b7c7910d2");
    }
    const paths = {
      "vega": "https://cdn.jsdelivr.net/npm//vega@5?noext",
      "vega-lib": "https://cdn.jsdelivr.net/npm//vega-lib?noext",
      "vega-lite": "https://cdn.jsdelivr.net/npm//vega-lite@4.17.0?noext",
      "vega-embed": "https://cdn.jsdelivr.net/npm//vega-embed@6?noext",
    };

    function maybeLoadScript(lib, version) {
      var key = `${lib.replace("-", "")}_version`;
      return (VEGA_DEBUG[key] == version) ?
        Promise.resolve(paths[lib]) :
        new Promise(function(resolve, reject) {
          var s = document.createElement('script');
          document.getElementsByTagName("head")[0].appendChild(s);
          s.async = true;
          s.onload = () => {
            VEGA_DEBUG[key] = version;
            return resolve(paths[lib]);
          };
          s.onerror = () => reject(`Error loading script: ${paths[lib]}`);
          s.src = paths[lib];
        });
    }

    function showError(err) {
      outputDiv.innerHTML = `<div class="error" style="color:red;">${err}</div>`;
      throw err;
    }

    function displayChart(vegaEmbed) {
      vegaEmbed(outputDiv, spec, embedOpt)
        .catch(err => showError(`Javascript Error: ${err.message}<br>This usually means there's a typo in your chart specification. See the javascript console for the full traceback.`));
    }

    if(typeof define === "function" && define.amd) {
      requirejs.config({paths});
      require(["vega-embed"], displayChart, err => showError(`Error loading script: ${err.message}`));
    } else {
      maybeLoadScript("vega", "5")
        .then(() => maybeLoadScript("vega-lite", "4.17.0"))
        .then(() => maybeLoadScript("vega-embed", "6"))
        .catch(showError)
        .then(() => displayChart(vegaEmbed));
    }
  })({"config": {"view": {"continuousWidth": 400, "continuousHeight": 300}}, "data": {"name": "data-dd9fd859cdad3a09d77f58896ce38134"}, "mark": "bar", "encoding": {"color": {"field": "hotel_star_rating", "type": "nominal"}, "tooltip": [{"field": "holiday_destination", "type": "nominal"}, {"field": "hotel_star_rating", "type": "quantitative"}], "x": {"field": "average_review_score", "type": "quantitative"}, "y": {"field": "country", "type": "nominal"}}, "$schema": "https://vega.github.io/schema/vega-lite/v4.17.0.json", "datasets": {"data-dd9fd859cdad3a09d77f58896ce38134": [{"holiday_destination": "Burj Khalifa", "most_visited_city": "Dubai", "country": "UAE", "all_inclusive_package": 20, "feedback_score": "Excellent", "hotel_star_rating": 4.7, "average_review_score": 9.6}, {"holiday_destination": "MGM Grand", "most_visited_city": "Las Vegas", "country": "USA", "all_inclusive_package": 15, "feedback_score": "Very Good", "hotel_star_rating": 4.0, "average_review_score": 8.9}, {"holiday_destination": "Tower Bridge", "most_visited_city": "London", "country": "UK", "all_inclusive_package": 9, "feedback_score": "Excellent", "hotel_star_rating": 4.7, "average_review_score": 8.6}, {"holiday_destination": "Tokyo Skytree", "most_visited_city": "Tokyo", "country": "Japan", "all_inclusive_package": 16, "feedback_score": "Very Good", "hotel_star_rating": 4.4, "average_review_score": 8.4}, {"holiday_destination": "Palolem Beach", "most_visited_city": "Goa", "country": "India", "all_inclusive_package": 21, "feedback_score": "Excellent", "hotel_star_rating": 4.6, "average_review_score": 8.2}, {"holiday_destination": "Khao Rang", "most_visited_city": "Phuket", "country": "Thailand", "all_inclusive_package": 12, "feedback_score": "Very Good", "hotel_star_rating": 4.5, "average_review_score": 7.3}, {"holiday_destination": "Mount Batur", "most_visited_city": "Bali", "country": "Indonesia", "all_inclusive_package": 7, "feedback_score": "Excellent", "hotel_star_rating": 4.6, "average_review_score": 8.2}, {"holiday_destination": "Escadaria Selar\u00f3n", "most_visited_city": "Rio de Janeiro", "country": "Brazil", "all_inclusive_package": 25, "feedback_score": "Excellent", "hotel_star_rating": 4.6, "average_review_score": 8.2}, {"holiday_destination": "Grouse Mountain", "most_visited_city": "Vancouver", "country": "Canada", "all_inclusive_package": 18, "feedback_score": "Excellent", "hotel_star_rating": 4.5, "average_review_score": 7.5}, {"holiday_destination": "Lovrijenac", "most_visited_city": "Dubrovnik", "country": "Croatia", "all_inclusive_package": 8, "feedback_score": "Excellent", "hotel_star_rating": 4.7, "average_review_score": 8.6}, {"holiday_destination": "Red Beach", "most_visited_city": "Santorini", "country": "Greece", "all_inclusive_package": 19, "feedback_score": "Very Good", "hotel_star_rating": 4.1, "average_review_score": 6.9}, {"holiday_destination": "D\u00fcden Waterfalls", "most_visited_city": "Antalya", "country": "Turkey", "all_inclusive_package": 15, "feedback_score": "Excellent", "hotel_star_rating": 4.7, "average_review_score": 8.3}, {"holiday_destination": "Colosseum", "most_visited_city": "Rome", "country": "Italy", "all_inclusive_package": 17, "feedback_score": "Excellent", "hotel_star_rating": 4.7, "average_review_score": 7.5}, {"holiday_destination": "Opera House", "most_visited_city": "Sydney", "country": "Australia", "all_inclusive_package": 10, "feedback_score": "Excellent", "hotel_star_rating": 4.7, "average_review_score": 9.3}, {"holiday_destination": "Vondelpark", "most_visited_city": "Amsterdam", "country": "Netherlands", "all_inclusive_package": 6, "feedback_score": "Excellent", "hotel_star_rating": 4.7, "average_review_score": 8.3}]}}, {"mode": "vega-lite"});
</script>




```python
# I found Data Visualisation module very challenging, initially found various datasets on kaggle and tried to use Tableau, 
# however even after using the guide and YouTube tips, I still found it quite difficult to use it. Then, I attempted the Altair
# method, so far it's much easier to understand. I chose an easier dataset, following the holiday destination homework in Pandas
# but adding more details then converting it into a CSV file. When I tried importing my file, I kept receiving a unicode error,
# after some research and going through my files, I've found that converting my regular CSV file to a CSV-UTF-8 fixed the 
# unicode error I kept receiving on Jupyter Notebook. After researching on some graphs, I really loved the look of circlePlot
# and stackbarPlot, however I knew because I don't have much data to work with, for the most parts it will look incomplete. 
# If I were to do this again, I would keep the feedback_score and hotel_star_rating balanced rather than just keeping the 
# values really high, so the graphs would not feel incomplete. 
```
