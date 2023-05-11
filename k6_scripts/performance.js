import http from 'k6/http';
import { check } from 'k6';

export let options = {
  vus: 100,
  duration: '60s'
}

export default function () {
  let response = http.get(`${__ENV.MY_HOSTNAME}`);
  check(response, {
    "Status 200 (OK)": (res) => res.status === 200,
  });

}
