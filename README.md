# auto-diagram
Creating a layer of automation for diagram creation

## API Design

The API for this application is documented in the `spec` directory. We are tentatively planning to provide a REST API for creating diagrams. Ansible could send requests to this API when creating a new environment. Alternately, we might choose to treat this as a build step. In that case, we'd keep the data structure defined in `spec` but discard the REST API endpoints.

The data would come from a combination of Ansible inventories (e.g., the environment names) and data provided by the engagement lead (e.g. the company name).

In the future, multiple tools could potentially consume the same data. For example, we might generate documentation as well as diagrams.

We're following the philosophy laid out in [Consumer-Driven Contracts](https://martinfowler.com/articles/consumerDrivenContracts.html) to ensure that our API is meaningful and extensible. In particular:

- Provide just the data that the consumer (the diagram generator) needs, not all the info that Ansible has to offer.
- Expect the consumer to ignore new fields that it doesn't understand. That way, we could update the API without breaking consumers that aren't able to update right away.

The API is versioned using [Semver](https://semver.org/). Backwards-compatible feature updates (e.g., new properties added) are indicated by minor releases. Breaking changes (e.g., an endpoint is renamed or a property is removed) are indicated by major releases.

## Taking a Screenshot via Headless Chrome
- $ google-chrome --headless --remote-debugging-port=9222
- $ node headless_chrome/screenshot.js 

## Front-end dev resources

- https://learnlayout.com/
- https://vuesjs.org/v2/guide/index.html
- https://github.com/axios/axios
- https://www.npmjs.com/package/live-server
