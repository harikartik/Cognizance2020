# Methods for plotting using Matplotlib                        ![logo](https://th.bing.com/th/id/OIP.SH1yNaY5RBheOFnOu_oGvwHaBx?pid=Api&rs=1)
---

## 1. Bar Chart

```python
  bar_chart(x,y,xLabel,yLabel,Title)
```

* __x__ - *Represents categories of horizontal axis*
* __y__ - *Represents datapoints of vertical axis*
* __xLabel__ - *Category of datapoints plotted along horizontal axis*
* __yLabel__ - *Category of datapoints plotted along vertical axis*
* __Title__ - *Heading of the bar chart*

` Example:`

### Sales of Products
---
|products|sales|
|---|---|
|shampoo|200|
|soap|350|
|conditioner|400|
|brush|600|

```python
  bar_chart(["shampoo","soap","conditioner","brush"], [200,350,400,600], "products", "sales", "Sales of Products")
```

![Bar chart](https://3.bp.blogspot.com/-vhJS_AqSbVM/W6D9HkeOVEI/AAAAAAAABH0/ZWcla0LK_cQyfXsnHeMGhJxyTHcmBnCCACLcBGAs/s1600/bar1.PNG)


## 2. Line Chart

```python
  Line_chart(x,y,xLabel,yLabel ,Title)
```

* __x__ - *Represents categories of horizontal axis*
* __y__ - *Represents datapoints of vertical axis*
* __xLabel__ - *Category of datapoints plotted along horizontal axis*
* __yLabel__ - *Category of datapoints plotted along vertical axis*
* __Title__ - *Heading of the line chart*

`Example`

### With Labels
---
|I am x|I am y|
|---|---|
|-1.00|-1.0|
|-0.50|0.0|
|0.00|1.0|
|0.50|2.0|
|1.00|3.0|

```python
  Line_chart([-1.00,-0.50,0.00,0.50,1.00],[-1.0,0.0,1.0,2.0,3.0],"I am x","I am y","With Labels")
```

![line chart](https://d33wubrfki0l68.cloudfront.net/077f05961cfc512d7c0473d75b398ce201e3b530/3c537/wp-content/uploads/2019/07/line-labels.png)


## 3. Pie Chart

```python
  pie_chart(x,Label,Title)
```

* __x__ - *Corresponding values of the categories*
* __Label__ - *List of categories*
* __Title__ - *Heading of the pie chart*

`Example`

### Shortstop
---
|Categoties|percent|
|---|---|
| Ozzie Smith | 17.8 |
| Marty Marion | 6.5 |
| Edgar Renteria | 58.8 |
| Dal Maxvill | 3.2 |
| David Eckstein | 13.7 |

```python
  pie_chart([17.8,6.5,58.8,3.2,13.7],["Ozzie Smith","Marty Marion","Edgar Renteria","Dal Maxvill","David Eckstein"],"Shortstop")
```

![pie chart](http://cdn2.vox-cdn.com/assets/4578425/image__9_.png)
