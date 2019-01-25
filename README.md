# Pandas-to-Production

Hackweek project 2019: Dataframes to React.

Create charts that can be displayed using the same React components both in Jupyter and in a standalone application.

- Create `Page`s with `Scatterplot`s, `Title`s, and more.
- `p2p.show([mypage])` to render in Jupyter using React components.
- `p2p.publish([mypage])` to publish to and render in a standalone app using the same React components.

## Getting Started

1. Install `docker` and `docker-compose`.

1. Build and start the stack.

   ```bash
   make all
   ```

1. View the stack.

   | App         | URL                       |
   | ----------- | ------------------------- |
   | Frontend    | http://localhost/         |
   | Backend API | http://localhost/api/     |
   | Swagger UI  | http://localhost/swagger/ |
   | Jupyter     | http://localhost:8888/    |

1. Navigate to Jupyter in your browser.

1. Open the `pandastoproduction.ipynb` notebook, which showcases the `pandastoproduction` (or `p2p`) Python library.

1. Run every step in the notebook.

   - `p2p.show(...)` will render the pages in the Jupyter notebook.
   - `p2p.publish(...)` will store the pages in a remote site (`localhost`) for viewing outside of Jupyter.

1. Navigate to the published page in your browser to view it outside of Jupyter.
