import streamlit as st
import pickle as pkl
import pandas as pd 

data_path = "data\\gemstone.csv"

data = pd.read_csv(data_path)

bar = st.sidebar.radio("Navigator", ["Home", "Prediction", "Data", "Contribute to Dataset"])
best_model = pkl.load(open("Models\\RidgeRegression.pkl", "rb"))

if bar == "Home": 
    st.write('''###  Introduction About the Data ''')
    st.image("data\\diamond.png", width=600)
    st.write("""
**The dataset** : The goal is to predict `price` of given diamond (Regression Analysis).

There are 10 independent variables (including `id`):

* `id` : unique identifier of each diamond
* `carat` : Carat (ct.) refers to the unique unit of weight measurement used exclusively to weigh gemstones and diamonds.
* `cut` : Quality of Diamond Cut
* `color` : Color of Diamond
* `clarity` : Diamond clarity is a measure of the purity and rarity of the stone, graded by the visibility of these characteristics under 10-power magnification.
* `depth` : The depth of diamond is its height (in millimeters) measured from the culet (bottom tip) to the table (flat, top surface)
* `table` : A diamond's table is the facet which can be seen when the stone is viewed face up.
* `x` : Diamond X dimension
* `y` : Diamond Y dimension
* `x` : Diamond Z dimension

Target variable:
* `price`: Price of the given Diamond.
""")

if bar == "Prediction":
    st.header("Diamond Price Prediction")
    st.image("data\\diamond2.png", width=600)
    
    carat = st.number_input("Carat", min_value=0.200000, max_value=3.500000, value=0.790688)

    st.write('''
             "Choose Cut category : "
             * **Fair** - 1, **Good** - 2, **Very Good** - 3, **Premium** - 4, **Ideal** - 5
             ''')
    cut = st.selectbox("cut", [1,2,3,4,5])

    st.write('''
        For Color Scheme : \n
        * **D** - 1, **E** - 2, **F** - 3, **G** - 4, **H** - 5, **I** - 6, **J** - 7
    ''')
    color = st.selectbox("color", [1,2,3,4,5,6,7])

    st.write('''
          For Clarity : \n
           * **I1** - 1,  **SI2** - 2,  **SI1** - 3,  **VS2** - 4,  **VS1** - 5, \n
           **VVS2** - 6,  **VVS1** - 7,  **IF** - 8
    ''')
    clarity = st.selectbox("clarity", [1,2,3,4,5,6,7,8])
    st.write('''
       * **depth** : (52.10 - 71.60)
    ''')
    depth = st.number_input("depth", min_value=52.100000, max_value=71.600000, value=61.820574)
    st.write('''
       * **table** : (49.00 - 79.00)
    ''')
    table = st.number_input("table", min_value=49.00, max_value=79.00,value=57.227675)
    
    st.write("Enter Dimensions of Diamond")
    st.write('''
       * x : (0.00 - 9.65)
       * y : (0.00 - 10.01)
       * z : (0.00 - 31.30)
    ''')
    x = st.number_input("x", min_value=0.00, max_value=9.650000	, value=5.715312)
    y = st.number_input("y", min_value=0.00, max_value=10.010000, value=5.720094)
    z = st.number_input("z", min_value=0.00, max_value=31.300000, value=3.534246)
    
    if st.button("Calculate Price"):
        data = [[carat, cut, color, clarity, depth, table, x, y, z]]
        price = best_model.predict(data)
        st.success(f"Price of your Diamond id {price}")
        st.balloons()


if bar == "Data":
    st.header("Diamond Price Prediction Dataset")
    st.dataframe(data)
