// axios
import axios from 'axios'


// const domain = "https://sandbox.scocug.com"
const domain = "http://127.0.0.1:8000"
const prefix = "api"

export const TIME_OUT = 80000
const ROOT_URL = `${domain}/${prefix}`
/*const token = localStorage.getItem('webToken')
let headers = {
  "Content-Type": "multipart/form-data"
}
if (token){
  headers.Authorization = `Basic ${token}`
}*/

const client = axios.create()
client.defaults.timeout = TIME_OUT;
client.defaults.baseURL = ROOT_URL;
export default client
