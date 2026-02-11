# Moving Averages (MAs)

  **Moving Averages** are a form of _momentum index_ in the sense that they do not add new information to an
  analysis, just present data in a different form. In the case of moving averages, they reduce the noise from
  short-term oscillations and help give up a better understanding of an underlying trend (if any). There are
  several uses of moving averages namely:
    
  1. Determining price extremes
  2. Determining support and resistance
  3. Determining Trend

  The most common use is in **determining trends**.

  This folder contains the implementation of the following moving averages:
    
  - **Simple Moving Average (SMA)**
  - **Linear Weighted Moving Average (LWMA)**
  - **Exponential Moving Average (EMA)**
  - **Wilder Method**
    
### Key Notes
  - As you will see (or have seen) from the implementation, the moving average is based on past prices and as
  such, is a lagging indicator. Using a moving average will always give us some delay in signaling a trend change
    
  - MAs are especially useful in markets that have a tendency to trend
    
  - In a nutshell, a moving average is just one number that represents a net of certain past numbers (prices). As
  such, it filters out each one of the prices during the past say 20 days and tells us how the _group_ of 20 days
  is behaving, rather than its separate parts. Remeber they are Moving **AVERAGES**