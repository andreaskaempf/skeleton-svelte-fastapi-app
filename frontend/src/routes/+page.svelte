<script>

// The current time, when changed updates on page
let curtime = "(nothing)";

// Get time from backend, when button is clicked
async function getData() {
    const json = await fetch("http://0.0.0.0:8000/query")
        .then(resp => resp.json());
    curtime = json.time;
}

</script>

<h1>Demo App</h1>

<p>Click the button to fetch the time:
  <button on:click={getData}>Click</button></p>

<p>Current time: {curtime}</p>
