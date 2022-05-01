# COMP30910 - FYP

This repository contains all code, data and microservices developed as part of the final year project entitled *Modelling Soil Compaction Based On Soil Moisture, Bulk Density And Other Soil Parameters*. All work has been completed by Ciarán Flanagan unless otherwise mentioned in the report.

The repository contains two microservices and a frontend. Both microservices are run in a similar manner, but need to be run on different ports. The Linear Regression microservice is located in `./linear-regression` and the SVR microservice is located in `./svr`.

# Running The Microservices
1. `cd` into the respective microservice
2. The `FLASK_APP` environmental variable first needs to be set with `export FLASK_APP=main`.
3. The microservice can now be run using `flask run --port=5001`
**Note:** If running both microservices, they will need to be run on separate ports. For example, `--port=5002` can be used for the second microservice.

# Running The Vue Frontend
1. Enter the frontend client directory via `cd ./client`
2. The frontend can then be started using `npm run serve`
3. The localhost URL will then be displayed, usually [localhost:8080](http://localhost:8080/).

# Models
All models can be found in their respective `.ipynb` Jupyter Notebook files. Any updates to these models will need to be exported to their respective
microservices. See the report for more on how to export the models from the Jupyter Notebooks to the microservices.