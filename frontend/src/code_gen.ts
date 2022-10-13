export enum Language {
  Node,
  Ruby,
  Php,
  C,
  Csharp,
  Cplusplus,
  Clojure,
  Go,
  Java,
  JavaScript,
  Kotlin,
  ObjectiveC,
  OCaml,
  Python,
  R,
  Swift,
}

export enum Method {
  Get,
  Post,
}

export class CodeGen {
  private url: string;

  constructor(url = "https://exmaple.com") {
    this.url = url;
  }

  getMdString(str: string) {
    return ` \`\`\`
        ${str}
        \`\`\`
        `;
  }

  getRequestUrl(params: any) {
    const url = this.url;
    const paramsArray: any[] = [];
    for (const [key, value] of Object.entries(params)) {
      paramsArray.push(`${key}=${value}`);
    }

    return `${url}?${paramsArray.join("&")}`;
  }

  getPostParam(params: any, language: Language) {
    if (language === Language.Node) {
      const paramsArray: any[] = [];
      for (const [key, value] of Object.entries(params)) {
        paramsArray.push(`${key}: '${value}'`);
      }

      return `{${paramsArray.join(",")}}`;
    } else if (language === Language.Ruby) {
      const paramsArray: any[] = [];
      for (const [key, value] of Object.entries(params)) {
        paramsArray.push(`\\"${key}\\": \\"${value}\\"`);
      }

      return `{${paramsArray.join(",")}}`;
    } else if (language === Language.Php) {
      const paramsArray: any[] = [];
      for (const [key, value] of Object.entries(params)) {
        paramsArray.push(`\\"${key}\\": \\"${value}\\"`);
      }

      return `{${paramsArray.join(",")}}`;
    } else if (language === Language.C) {
      const paramsArray: any[] = [];
      for (const [key, value] of Object.entries(params)) {
        paramsArray.push(`\\"${key}\\": \\"${value}\\"`);
      }

      return `{${paramsArray.join(",")}}`;
    } else if (language === Language.Csharp) {
      const paramsArray: any[] = [];
      for (const [key, value] of Object.entries(params)) {
        paramsArray.push(`\\"${key}\\": \\"${value}\\"`);
      }

      return `{${paramsArray.join(",")}}`;
    } else if (language === Language.Cplusplus) {
      const paramsArray: any[] = [];
      for (const [key, value] of Object.entries(params)) {
        paramsArray.push(`\\"${key}\\": \\"${value}\\"`);
      }

      return `{${paramsArray.join(",")}}`;
    } else if (language === Language.Go) {
      const paramsArray: any[] = [];
      for (const [key, value] of Object.entries(params)) {
        paramsArray.push(`\\"${key}\\": \\"${value}\\"`);
      }

      return `{${paramsArray.join(",")}}`;
    } else if (language === Language.Clojure) {
      const paramsArray: any[] = [];
      for (const [key, value] of Object.entries(params)) {
        paramsArray.push(`:${key} "${value}"`);
      }

      return `{${paramsArray.join("\n")}}`;
    } else if (language === Language.Java) {
      const paramsArray: any[] = [];
      for (const [key, value] of Object.entries(params)) {
        paramsArray.push(`\\"${key}\\": \\"${value}\\"`);
      }

      return `{${paramsArray.join(",")}}`;
    } else if (language === Language.JavaScript) {
      const paramsArray: any[] = [];
      for (const [key, value] of Object.entries(params)) {
        paramsArray.push(`${key}: '${value}'`);
      }

      return `{${paramsArray.join(",")}}`;
    } else if (language === Language.ObjectiveC) {
      const paramsArray: any[] = [];
      for (const [key, value] of Object.entries(params)) {
        paramsArray.push(`@"${key}": @"${value}"`);
      }

      return `{${paramsArray.join(",")}}`;
    } else if (language === Language.OCaml) {
      const paramsArray: any[] = [];
      for (const [key, value] of Object.entries(params)) {
        paramsArray.push(`\\"${key}\\": \\"${value}\\"`);
      }

      return `{${paramsArray.join(",")}}`;
    } else if (language === Language.Python) {
      const paramsArray: any[] = [];
      for (const [key, value] of Object.entries(params)) {
        paramsArray.push(`"${key}": "${value}"`);
      }

      return `{${paramsArray.join(",")}}`;
    } else if (language === Language.R) {
      const paramsArray: any[] = [];
      for (const [key, value] of Object.entries(params)) {
        paramsArray.push(`\\"${key}\\": \\"${value}\\"`);
      }

      return `{${paramsArray.join(",")}}`;
    } else if (language === Language.Swift) {
      const paramsArray: any[] = [];
      for (const [key, value] of Object.entries(params)) {
        paramsArray.push(`"${key}": "${value}"`);
      }

      return `[${paramsArray.join(",")}] as [String : Any]`;
    }
    return "";
  }

  generateCode(method: Method, language: Language, params: any, isMd: boolean) {
    let code = "";
    if (method === Method.Get) {
      const url = this.getRequestUrl(params);
      if (language === Language.Node) {
        code = `
const sdk = require('api')('${url}');

sdk.actsAll({page: '1'})
  .then(res => console.log(res))
  .catch(err => console.error(err));
                `;
      } else if (language === Language.Ruby) {
        code = `
require 'uri'
require 'net/http'
require 'openssl'

url = URI("${url}")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)
request["accept"] = 'application/json'

response = http.request(request)
puts response.read_body
                `;
      } else if (language === Language.Php) {
        code = `
<?php
require_once('vendor/autoload.php');

$client = new GuzzleHttpClient();

$response = $client->request('GET', '${url}', [
  'headers' => [
    'accept' => 'application/json',
  ],
]);

echo $response->getBody();
                `;
      } else if (language === Language.C) {
        code = `
CURL *hnd = curl_easy_init();

curl_easy_setopt(hnd, CURLOPT_CUSTOMREQUEST, "GET");
curl_easy_setopt(hnd, CURLOPT_URL, "${url}");

struct curl_slist *headers = NULL;
headers = curl_slist_append(headers, "accept: application/json");
curl_easy_setopt(hnd, CURLOPT_HTTPHEADER, headers);

CURLcode ret = curl_easy_perform(hnd);
                `;
      } else if (language === Language.Csharp) {
        code = `
var client = new RestClient("${url}");
var request = new RestRequest(Method.GET);
request.AddHeader("accept", "application/json");
IRestResponse response = client.Execute(request);
                `;
      } else if (language === Language.Cplusplus) {
        code = `
CURL *hnd = curl_easy_init();

curl_easy_setopt(hnd, CURLOPT_CUSTOMREQUEST, "GET");
curl_easy_setopt(hnd, CURLOPT_URL, "${url}");

struct curl_slist *headers = NULL;
headers = curl_slist_append(headers, "accept: application/json");
curl_easy_setopt(hnd, CURLOPT_HTTPHEADER, headers);

CURLcode ret = curl_easy_perform(hnd);
                `;
      } else if (language === Language.Clojure) {
        code = `
(require '[clj-http.client :as client])

(client/get "${url}" {:accept :json})
                `;
      } else if (language === Language.Go) {
        code = `
package main

import (
	"fmt"
	"net/http"
	"io/ioutil"
)

func main() {

	url := "${url}"

	req, _ := http.NewRequest("GET", url, nil)

	req.Header.Add("accept", "application/json")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := ioutil.ReadAll(res.Body)

	fmt.Println(res)
	fmt.Println(string(body))

}
                `;
      } else if (language === Language.Java) {
        code = `
OkHttpClient client = new OkHttpClient();

Request request = new Request.Builder()
  .url("${url}")
  .get()
  .addHeader("accept", "application/json")
  .build();

Response response = client.newCall(request).execute();
                `;
      } else if (language === Language.JavaScript) {
        code = `
const options = {method: 'GET', headers: {accept: 'application/json'}};

fetch('${url}', options)
  .then(response => response.json())
  .then(response => console.log(response))
  .catch(err => console.error(err));
                `;
      } else if (language === Language.Kotlin) {
        code = `
val client = OkHttpClient()

val request = Request.Builder()
  .url("${url}")
  .get()
  .addHeader("accept", "application/json")
  .build()

val response = client.newCall(request).execute()
                `;
      } else if (language === Language.Python) {
        code = `
import requests

url = "${url}"

headers = {"accept": "application/json"}

response = requests.get(url, headers=headers)

print(response.text)
                `;
      } else if (language === Language.R) {
        code = `
library(httr)

url <- "${url}"

queryString <- list(page = "1")

response <- VERB("GET", url, query = queryString, content_type("application/octet-stream"), accept("application/json"))

content(response, "text")
                `;
      } else if (language === Language.Swift) {
        code = `
import Foundation

let headers = ["accept": "application/json"]

let request = NSMutableURLRequest(url: NSURL(string: "${url}")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "GET"
request.allHTTPHeaderFields = headers

let session = URLSession.shared
let dataTask = session.dataTask(with: request as URLRequest, completionHandler: { (data, response, error) -> Void in
  if (error != nil) {
    print(error as Any)
  } else {
    let httpResponse = response as? HTTPURLResponse
    print(httpResponse)
  }
})

dataTask.resume()
                `;
      }
      if (isMd) {
        code = this.getMdString(code);
      }
      return code;
    }
    if (method === Method.Post) {
      const paramsString = this.getPostParam(params, language);
      if (language === Language.Node) {
        code = `
const sdk = require('api')('${this.url}');

sdk.actCreate(${paramsString})
  .then(res => console.log(res))
  .catch(err => console.error(err));
                `;
      } else if (language === Language.Ruby) {
        code = `
require 'uri'
require 'net/http'
require 'openssl'

url = URI("${this.url}")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["accept"] = 'application/json'
request["content-type"] = 'application/json'
request.body = "${paramsString}"

response = http.request(request)
puts response.read_body
                `;
      } else if (language === Language.Php) {
        code = `
<?php

$curl = curl_init();

curl_setopt_array($curl, [
  CURLOPT_URL => "${this.url}",
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => "",
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 30,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => "POST",
  CURLOPT_POSTFIELDS => "${paramsString}",
  CURLOPT_HTTPHEADER => [
    "accept: application/json",
    "content-type: application/json"
  ],
]);

$response = curl_exec($curl);
$err = curl_error($curl);

curl_close($curl);

if ($err) {
  echo "cURL Error #:" . $err;
} else {
  echo $response;
}
                `;
      } else if (language === Language.C) {
        code = `
CURL *hnd = curl_easy_init();

curl_easy_setopt(hnd, CURLOPT_CUSTOMREQUEST, "POST");
curl_easy_setopt(hnd, CURLOPT_URL, "${this.url}");

struct curl_slist *headers = NULL;
headers = curl_slist_append(headers, "accept: application/json");
headers = curl_slist_append(headers, "content-type: application/json");
curl_easy_setopt(hnd, CURLOPT_HTTPHEADER, headers);

curl_easy_setopt(hnd, CURLOPT_POSTFIELDS, "${paramsString}");

CURLcode ret = curl_easy_perform(hnd);
                `;
      } else if (language === Language.Csharp) {
        code = `
using System.Net.Http.Headers;
var client = new HttpClient();
var request = new HttpRequestMessage
{
    Method = HttpMethod.Post,
    RequestUri = new Uri("${this.url}"),
    Headers =
    {
        { "accept", "application/json" },
    },
    Content = new StringContent("${paramsString}")
    {
        Headers =
        {
            ContentType = new MediaTypeHeaderValue("application/json")
        }
    }
};
using (var response = await client.SendAsync(request))
{
    response.EnsureSuccessStatusCode();
    var body = await response.Content.ReadAsStringAsync();
    Console.WriteLine(body);
}
                `;
      } else if (language === Language.Cplusplus) {
        code = `
CURL *hnd = curl_easy_init();

curl_easy_setopt(hnd, CURLOPT_CUSTOMREQUEST, "POST");
curl_easy_setopt(hnd, CURLOPT_URL, "${this.url}");

struct curl_slist *headers = NULL;
headers = curl_slist_append(headers, "accept: application/json");
headers = curl_slist_append(headers, "content-type: application/json");
curl_easy_setopt(hnd, CURLOPT_HTTPHEADER, headers);

curl_easy_setopt(hnd, CURLOPT_POSTFIELDS, "${paramsString}");

CURLcode ret = curl_easy_perform(hnd);
                `;
      } else if (language === Language.Clojure) {
        code = `
(require '[clj-http.client :as client])

(client/post "${this.url}" {:content-type :json
                                               :form-params ${paramsString}
                                               :accept :json})
                `;
      } else if (language === Language.Go) {
        code = `
package main

import (
	"fmt"
	"strings"
	"net/http"
	"io/ioutil"
)

func main() {

	url := "${this.url}"

	payload := strings.NewReader("${paramsString}")

	req, _ := http.NewRequest("POST", url, payload)

	req.Header.Add("accept", "application/json")
	req.Header.Add("content-type", "application/json")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := ioutil.ReadAll(res.Body)

	fmt.Println(res)
	fmt.Println(string(body))

}
                `;
      } else if (language === Language.Java) {
        code = `
AsyncHttpClient client = new DefaultAsyncHttpClient();
client.prepare("POST", "${this.url}")
  .setHeader("accept", "application/json")
  .setHeader("content-type", "application/json")
  .setBody("${paramsString}")
  .execute()
  .toCompletableFuture()
  .thenAccept(System.out::println)
  .join();

client.close();
                `;
      } else if (language === Language.JavaScript) {
        code = `
import axios from 'axios';

const options = {
  method: 'POST',
  url: '${this.url}',
  headers: {accept: 'application/json', 'content-type': 'application/json'},
  data: ${paramsString}
};

axios
  .request(options)
  .then(function (response) {
    console.log(response.data);
  })
  .catch(function (error) {
    console.error(error);
  });
                `;
      } else if (language === Language.Kotlin) {
        code = `
val client = OkHttpClient()

val mediaType = MediaType.parse("application/json")
val body = RequestBody.create(mediaType, "${paramsString}")
val request = Request.Builder()
  .url("${this.url}")
  .post(body)
  .addHeader("accept", "application/json")
  .addHeader("content-type", "application/json")
  .build()

val response = client.newCall(request).execute()
                `;
      } else if (language === Language.Python) {
        code = `
import requests

url = "${this.url}"

payload = ${paramsString}
headers = {
    "accept": "application/json",
    "content-type": "application/json"
}

response = requests.post(url, json=payload, headers=headers)

print(response.text)
                `;
      } else if (language === Language.R) {
        code = `
library(httr)

url <- "${this.url}"

payload <- "${paramsString}"

encode <- "json"

response <- VERB("POST", url, body = payload, content_type("application/json"), accept("application/json"), encode = encode)

content(response, "text")
                `;
      } else if (language === Language.Swift) {
        code = `
import Foundation

let headers = [
  "accept": "application/json",
  "content-type": "application/json"
]
let parameters = ${paramsString}

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "${this.url}")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "POST"
request.allHTTPHeaderFields = headers
request.httpBody = postData as Data

let session = URLSession.shared
let dataTask = session.dataTask(with: request as URLRequest, completionHandler: { (data, response, error) -> Void in
  if (error != nil) {
    print(error as Any)
  } else {
    let httpResponse = response as? HTTPURLResponse
    print(httpResponse)
  }
})

dataTask.resume()
                `;
      }
      if (isMd) {
        code = this.getMdString(code);
      }
      return code;
    }
    return code;
  }
}
