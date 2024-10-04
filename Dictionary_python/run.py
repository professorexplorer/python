thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
# thisdict["year"].insert(1992)
thisdict.update({"year": 1992})
thisdict.update({"brand": "KIA"})
thisdict.pop("model")

print(thisdict)