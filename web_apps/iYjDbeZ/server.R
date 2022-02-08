library(shiny)
library(dataiku)

myGeoDataset <- dkuReadDataset("DKU_TSHIRTS.crm_history", samplingMethod="head", nbRows=1000)
puts(myGeoDataset)
shinyServer(function(input, output) {

  output$mymap <- renderLeaflet({
    leaflet(data = myGeoDataset) %>%
      addProviderTiles(providers$Stamen.TonerLite,
        options = providerTileOptions(noWrap = TRUE)
      ) %>%
      # Change "longitude" and "latitude"
      # for your corresponding column names if necessary:
      addMarkers(~longitude, ~latitude)
  })
})