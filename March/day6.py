import pandas as pd
import numpy as np

# String Manipulation

val="a, b , gudio"
print(val.split(","))

pieces=[x.strip() for x in val.split(",")]
print(pieces)

first, second, third=pieces
print(first+"::"+second+"::"+third)

print("::".join(pieces))

# Data Wrangling

data=pd.Series(np.random.uniform(size=9),
               index=[["a","a","a","b","b","b","c","c","c"],
                      [1,2,3,1,2,3,1,2,3]])
print(data)
print(data['b'][3])
print(data["a":"c"])
print(data.loc[["a","c"]])

print(data.unstack())

frame=pd.DataFrame(np.arange(12).reshape((4,3)),
                   index=[["a","a","b","b"],[1,2,1,3]],
                   columns=[["Ohio","Ohio","Coronada"],["Green","Red","Green"]])
print(frame)

frame.index.names=["key1","key2"]
frame.columns.names=["state","color"]
print(frame)
print(frame.index.nlevels)

# Combining df

df1=pd.DataFrame({"key":["b","b","a","c","a","a"],
                  "data1":[1,2,3,4,5,6]})
df2=pd.DataFrame({"key":["b","r","c"],
                  "data2":[12,34,34]})

df3=pd.DataFrame({"lkey":["b","b","a","c","a","a"],
                  "data1":[1,2,3,4,5,6]})
df4=pd.DataFrame({"rkey":["b","r","c"],
                  "data2":[12,34,34]})

print(pd.merge(df1,df2))
print(pd.merge(df3,df4, left_on="lkey", right_on="rkey"))

print(pd.merge(df1,df2, how="outer"))
print(pd.merge(df3,df4, left_on="lkey", right_on="rkey", how="outer"))

print(pd.merge(df1,df2, how="left"))

# Concatination

arr=np.arange(12).reshape((3,4))
print(np.concatenate([arr,arr], axis=1))
print(np.concatenate([arr,arr]))

s1=pd.Series([0,1], index=["a","b"], dtype="Int64")
s2=pd.Series([2,3,4], index=["c","d","e"], dtype="Int64")
s3=pd.Series([5,6], index=["f","g"], dtype="Int64")
s4=pd.Series([5,6], index=["f","g"], dtype="Int64")

print(pd.concat([s1,s2,s3,s4]))
print(pd.concat([s1,s2,s3,s4], axis="columns"))


a=pd.Series([np.nan,2.5,3.5,4.5,6.,np.nan],
            index=["a","h","i","g","k","l"])
b=pd.Series([4.,2.5,np.nan,4.5,np.nan,7.1],
            index=["l","k","a","i","h","g"])

print(a)
print(b)

print(np.where(pd.isna(a), b, a))
print(a.combine_first(b))

# Ploting and visualization

from matplotlib import pyplot as plt

data=np.arange(10)
# plt.plot(data)

fig=plt.figure()
ax1=fig.add_subplot(2,2,1)
ax1.hist(np.random.standard_normal(100), bins=20,color="black",alpha=0.6)

ax2=fig.add_subplot(2,2,2)
ax2.scatter(np.arange(30), np.arange(30)+3*np.random.standard_normal(30))

ax3=fig.add_subplot(2,2,3)
ax3.plot(np.random.standard_normal(50).cumsum(), color="black",linestyle="dashed")

ax1=fig.add_subplot(2,2,4)

fig=plt.figure()
fig,ax=plt.subplots()

ax.plot(np.random.randn(1000).cumsum(),color="black",label="one")
ax.plot(np.random.randn(1000).cumsum(),linestyle="dotted",color="blue",label="two")
ax.plot(np.random.randn(1000).cumsum(),linestyle="dotted",color="red",label="three")

ax.legend()

plt.show()