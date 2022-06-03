
# get the base node image
FROM node:alpine as builder

# set the working dir for container
WORKDIR /frontend

# copy the json file first
COPY ./package.json /frontend

# install npm dependencies
RUN npm install

# copy other project files
COPY . .

# define build args
ARG API_URL
ARG GOOGLE_API_KEY

# build the folder
RUN REACT_APP_API_URL=$API_URL \
    REACT_APP_GOOGLE_API_KEY=$GOOGLE_API_KEY \
    npm run build

# Handle Nginx
FROM nginx
COPY --from=builder /frontend/build /usr/share/nginx/html
COPY ./nginx/default.conf /etc/nginx/conf.d/default.conf