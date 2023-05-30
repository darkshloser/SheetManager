import Vue from "vue";
import Router from "vue-router";
import store from "../store/index.js";


Vue.use(Router);


const router = new Router({
    mode: "history",
    routes: [
      {
        path: "/",
        name: "home",
        component: () =>
              import(/*webpackName: "HomePage"*/ "../views/HomePage")
      },
      {
        path: "/about",
        name: "about",
        component: () =>
              import(/*webpackName: "AboutPage"*/ "../views/AboutPage")
      },
      {
        path: "/dashboard",
        name: "dashboard",
        component: () =>
              import("../views/DashboardPage"),
        beforeEnter: (to, from, next) => {
          if (store.getters.isDataInSync) {
            next()
          } else {
            store.dispatch('getAllCsvs')
            .then(() => next())
            .catch(() => {
              store.dispatch('sendNotification', {
                heading: 'Error during retrieval of all CSV records.',
                duration: 7000,
              });
            })
          }
        }
      },
      {
        path: "/upload-csv",
        name: "upload",
        component: () =>
              import("../views/UploadPage")
      },
      {
        path: "/details/:name",
        name: "details",
        component: () =>
              import("../views/DetailsPage"),
        beforeEnter: (to, from, next) => {
          if (store.getters.isDataInSync) {
            next()
          } else {
            store.dispatch('getAllCsvs')
            .then(() => next())
            .catch(() => {
              store.dispatch('sendNotification', {
                heading: 'Error during retrieval of all CSV records.',
                duration: 7000,
              });
            })
          }
        }
      },
      {
        path: "/404",
        alias: "*",
        name: "notFound",
        component: () =>
          import(/* webpackChunkName: "NotFound" */ "../views/NotFound")
      }
    ]
});

  
export default router;
