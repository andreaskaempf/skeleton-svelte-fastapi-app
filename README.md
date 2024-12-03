# Simple Svelte+FastAPI App

This is a minimalist scaffolding app to run a Python+FastAPI backend
behind a Svelte frontend. There is only one page with a button, that
calls the backend for the time when pressed. That's it.

To run both the front and back ends, type `docker compose up --build`

## Backend

The backend is a very simple Python program that exposes two endpoints,
the root (/) and /query. Both return simple JSON objects.

Things to note:
* In backend/app/backend.py, CORS middleware is critical to allow the 
  frontend to call the backend, and the `allow_origins` parameter includes 
  the URLs of the frontend running both locally in development mode (port 
  5173) and the in build mode (port 3000)
* The Dockerfile exposes port 8000 (called by the frontend)
* The app is run by uvicorn, specifying host 0.0.0.0 and port 8000

You can test the backend on its own as follows:

```
docker build . -t backend
docker run -p 8000:8000
```

In a separate terminal, type `curl http://0.0.0.0:8000/query` to get a response

## Frontend

The frontend is a very minimalistic Sveltekit app, and was built as follows.

```
mkdir frontend
cd frontend
npx sv create
```

For the last command, hit enter for defaults, i.e., in current directory,
minimal template, no TypeScript (unless you want it), no extras, npm installer.

You can then already run `npm run dev` to test the minimal one-page example by
browsing to http://localhost:5173.

However, you should also enable "build mode" by first installing the node adapter, 
i.e., `npm i -D @svelte/adapter-node`. Then adjust svelte.config.js as follows:

```
import adapter from '@sveltejs/adapter-node';

const config = {
	kit: { adapter: adapter() }
};

export default config;
```

See frontend/src/routes/+page.svelte in this repository for an example of
how the frontend can call the backend. Note that the fetch should simply
call the URL of the endpoint, using host, port and path:

```
<script>
async function getData() {
    const json = await fetch("http://0.0.0.0:8000/query")
        .then(resp => resp.json());
    curtime = json.time;
}
</script>
```

In the Dockerfile for the frontend , note the following:
* We can use the minimalist Alpine Linux as the base
* Node is the server, as required by Svelte apps (the
  static adapter does not work for practical purposes)
* After copying things over, `npm install` adds the
  required dependencies, including the node-adapter
* `npm run build` creates the output files in the build 
  directory
* Port 3000 needs to be exposed
* The HOST environment variable needs to be 0.0.0.0
* The command to run the container in `node build`

Again, you can test by building the container and running it,
although the backend will need to be running for the button
to work.

## Putting it together

All of this is taken care of when you run 
`docker compose up --build` in the top level directory. This
runs both the front and backends in separate containers, at
the same time.

In the docker-compose.yml file, not the following:
* The frontend service is build from that directory, uses
  the port 3000 (can be mapped to 80 for production, i.e., change
  3000:3000 to 80:3000)
* The frontend includes `links: "backend:backend"`, not sure if
  this is required
* The backend service similarly uses port 8000:8000 and test-network
* The network test-network is simply a bridge

AK, 3 Dec 2024

