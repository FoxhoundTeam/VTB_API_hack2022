export const Language = {
  NODE: "NodeJS",
  RUBY: "Ruby",
  PHP: "PHP",
  C: "C",
  CSHARP: "C#",
  CPLUSPLUS: "C++",
  CLOJURE: "Clojure",
  GO: "Go",
  JAVA: "Java",
  JAVASCRIPT: "JavaScrip",
  KOTLIN: "Kotlin",
  PYTHON: "Python",
  R: "R",
  SWIFT: "Swift",
};

export const Method = {
  GET: "GET",
  POST: "POST",
  PUT: "PUT",
  DELETE: "DELETE",
  PATCH: "PATCH",
  OPTIONS: "OPTIONS",
  HEAD: "HEAD",
  COPY: "COPY",
  LINK: "LINK",
  UNLINK: "UNLINK",
  PURGE: "PURGE",
  LOCK: "LOCK",
  UNLOCK: "UNLOCK",
  PROPFIND: "PROPFIND",
  VIEW: "VIEW",
};
function ucFirst(str: string) {
  if (!str) return str;

  return str[0].toUpperCase() + str.slice(1);
}

export const MdCodeSupport = {
  NodeJS: "typescript",
  Ruby: "ruby",
  PHP: "php",
  C: "c",
  "C#": "csharp",
  "C++": "cplusplus",
  Clojure: "clojure",
  Go: "go",
  Java: "java",
  JavaScrip: "javascript",
  Kotlin: "kotlin",
  Python: "python",
  R: "r",
  Swift: "swift",
} as Record<string, string>;

export class CodeGen {
  constructor() {}

  getMdString(str: string, lang: string) {
    return `\`\`\`${MdCodeSupport[lang]}
        ${str}
\`\`\``;
  }

  getMethodString(method: string, lang: string) {
    let methodStr = method.toString();
    if (
      [
        Language.RUBY,
        Language.CSHARP,
        Language.KOTLIN,
        Language.PYTHON,
      ].includes(lang)
    ) {
      methodStr = ucFirst(methodStr);
    } else if (
      [
        Language.PHP,
        Language.C,
        Language.CPLUSPLUS,
        Language.GO,
        Language.JAVA,
        Language.JAVASCRIPT,
        Language.R,
        Language.SWIFT,
      ].includes(lang)
    ) {
      methodStr = methodStr.toUpperCase();
    } else if ([Language.CLOJURE].includes(lang)) {
      methodStr = methodStr.toLowerCase();
    }
    return methodStr;
  }

  getRequestUrl(pathParams: Object, url: string) {
    for (const [key, value] of Object.entries(pathParams)) {
      if (value === undefined) continue;
      url = url.replace(`{${key}}`, value);
    }

    return url;
  }

  addQueryParam(queryParams: Object, url: string) {
    const paramsArray: any[] = [];
    for (const [key, value] of Object.entries(queryParams)) {
      if (value === undefined) continue;
      paramsArray.push(`${key}=${value}`);
    }
    if (paramsArray.length == 0) return url;

    return `${url}?${paramsArray.join("&")}`;
  }

  getBodyParam(params: any, language: string) {
    if ([Language.NODE, Language.JAVASCRIPT].includes(language)) {
      const paramsArray: any[] = [];
      for (const [key, value] of Object.entries(params)) {
        if (typeof value == "object")
          paramsArray.push(`${key}: ${this.getBodyParam(value, language)}`);
        else paramsArray.push(`${key}: '${value}'`);
      }

      return `{${paramsArray.join(", ")}}`;
    } else if (
      [
        Language.RUBY,
        Language.PHP,
        Language.C,
        Language.CSHARP,
        Language.CPLUSPLUS,
        Language.GO,
        Language.JAVA,
        Language.R,
      ].includes(language)
    ) {
      const paramsArray: any[] = [];
      for (const [key, value] of Object.entries(params)) {
        if (typeof value == "object")
          paramsArray.push(
            `\\"${key}\\": ${this.getBodyParam(value, language)}`
          );
        else paramsArray.push(`\\"${key}\\": \\"${value}\\"`);
      }

      return `{${paramsArray.join(", ")}}`;
    } else if (language == Language.CLOJURE) {
      const paramsArray: any[] = [];
      for (const [key, value] of Object.entries(params)) {
        if (typeof value == "object")
          paramsArray.push(`:${key} ${this.getBodyParam(value, language)}`);
        else paramsArray.push(`:${key} "${value}"`);
      }

      return `{${paramsArray.join("\n")}}`;
    } else if ([Language.PYTHON, Language.SWIFT].includes(language)) {
      const paramsArray: any[] = [];
      for (const [key, value] of Object.entries(params)) {
        if (typeof value == "object")
          paramsArray.push(`"${key}": ${this.getBodyParam(value, language)}`);
        else paramsArray.push(`"${key}": "${value}"`);
      }

      return `{${paramsArray.join(", ")}}`;
    }
    return "{}";
  }

  generateCode({
    urlTemplate,
    method,
    language,
    isMd,
    pathParams,
    queryParams,
    body,
  }: {
    urlTemplate: string;
    method: string;
    language: string;
    isMd: boolean;
    pathParams?: Object;
    queryParams?: Object;
    body?: Object;
  }) {
    let code = "";
    if (method == Method.GET) {
      const urlPath = pathParams
        ? this.getRequestUrl(pathParams, urlTemplate)
        : urlTemplate;
      const url = queryParams
        ? this.addQueryParam(queryParams, urlPath)
        : urlPath;
      if (language == Language.NODE) {
        code = `
const sdk = require('api')('${url}');

sdk.actsAll({page: '1'})
  .then(res => console.log(res))
  .catch(err => console.error(err));
                `;
      } else if (language == Language.RUBY) {
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
      } else if (language == Language.PHP) {
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
      } else if (language == Language.C) {
        code = `
CURL *hnd = curl_easy_init();

curl_easy_setopt(hnd, CURLOPT_CUSTOMREQUEST, "GET");
curl_easy_setopt(hnd, CURLOPT_URL, "${url}");

struct curl_slist *headers = NULL;
headers = curl_slist_append(headers, "accept: application/json");
curl_easy_setopt(hnd, CURLOPT_HTTPHEADER, headers);

CURLcode ret = curl_easy_perform(hnd);
                `;
      } else if (language == Language.CSHARP) {
        code = `
var client = new RestClient("${url}");
var request = new RestRequest(Method.GET);
request.AddHeader("accept", "application/json");
IRestResponse response = client.Execute(request);
                `;
      } else if (language == Language.CPLUSPLUS) {
        code = `
CURL *hnd = curl_easy_init();

curl_easy_setopt(hnd, CURLOPT_CUSTOMREQUEST, "GET");
curl_easy_setopt(hnd, CURLOPT_URL, "${url}");

struct curl_slist *headers = NULL;
headers = curl_slist_append(headers, "accept: application/json");
curl_easy_setopt(hnd, CURLOPT_HTTPHEADER, headers);

CURLcode ret = curl_easy_perform(hnd);
                `;
      } else if (language == Language.CLOJURE) {
        code = `
(require '[clj-http.client :as client])

(client/get "${url}" {:accept :json})
                `;
      } else if (language == Language.GO) {
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
      } else if (language == Language.JAVA) {
        code = `
OkHttpClient client = new OkHttpClient();

Request request = new Request.Builder()
  .url("${url}")
  .get()
  .addHeader("accept", "application/json")
  .build();

Response response = client.newCall(request).execute();
                `;
      } else if (language == Language.JAVASCRIPT) {
        code = `
const options = {method: 'GET', headers: {accept: 'application/json'}};

fetch('${url}', options)
  .then(response => response.json())
  .then(response => console.log(response))
  .catch(err => console.error(err));
                `;
      } else if (language == Language.KOTLIN) {
        code = `
val client = OkHttpClient()

val request = Request.Builder()
  .url("${url}")
  .get()
  .addHeader("accept", "application/json")
  .build()

val response = client.newCall(request).execute()
                `;
      } else if (language == Language.PYTHON) {
        code = `
import requests

url = "${url}"

headers = {"accept": "application/json"}

response = requests.get(url, headers=headers)

print(response.text)
                `;
      } else if (language == Language.R) {
        code = `
library(httr)

url <- "${url}"

queryString <- list(page = "1")

response <- VERB("GET", url, query = queryString, content_type("application/octet-stream"), accept("application/json"))

content(response, "text")
                `;
      } else if (language == Language.SWIFT) {
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
        code = this.getMdString(code, language);
      }
      return code;
    } else {
      const url = pathParams
        ? this.getRequestUrl(pathParams, urlTemplate)
        : urlTemplate;
      const paramsString = this.getBodyParam(body, language);
      const methodString = this.getMethodString(method, language);
      if (language == Language.NODE) {
        code = `
const sdk = require('api')('${url}');

sdk.actCreate(${paramsString})
  .then(res => console.log(res))
  .catch(err => console.error(err));
                `;
      } else if (language == Language.RUBY) {
        code = `
require 'uri'
require 'net/http'
require 'openssl'

url = URI("${url}")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::${methodString}.new(url)
request["accept"] = 'application/json'
request["content-type"] = 'application/json'
request.body = "${paramsString}"

response = http.request(request)
puts response.read_body
                `;
      } else if (language == Language.PHP) {
        code = `
<?php

$curl = curl_init();

curl_setopt_array($curl, [
  CURLOPT_URL => "${url}",
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => "",
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 30,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => "${methodString}",
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
      } else if (language == Language.C) {
        code = `
CURL *hnd = curl_easy_init();

curl_easy_setopt(hnd, CURLOPT_CUSTOMREQUEST, "${methodString}");
curl_easy_setopt(hnd, CURLOPT_URL, "${url}");

struct curl_slist *headers = NULL;
headers = curl_slist_append(headers, "accept: application/json");
headers = curl_slist_append(headers, "content-type: application/json");
curl_easy_setopt(hnd, CURLOPT_HTTPHEADER, headers);

curl_easy_setopt(hnd, CURLOPT_POSTFIELDS, "${paramsString}");

CURLcode ret = curl_easy_perform(hnd);
                `;
      } else if (language == Language.CSHARP) {
        code = `
using System.Net.Http.Headers;
var client = new HttpClient();
var request = new HttpRequestMessage
{
    Method = HttpMethod.${methodString},
    RequestUri = new Uri("${url}"),
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
      } else if (language == Language.CPLUSPLUS) {
        code = `
CURL *hnd = curl_easy_init();

curl_easy_setopt(hnd, CURLOPT_CUSTOMREQUEST, "${methodString}");
curl_easy_setopt(hnd, CURLOPT_URL, "${url}");

struct curl_slist *headers = NULL;
headers = curl_slist_append(headers, "accept: application/json");
headers = curl_slist_append(headers, "content-type: application/json");
curl_easy_setopt(hnd, CURLOPT_HTTPHEADER, headers);

curl_easy_setopt(hnd, CURLOPT_POSTFIELDS, "${paramsString}");

CURLcode ret = curl_easy_perform(hnd);
                `;
      } else if (language == Language.CLOJURE) {
        code = `
(require '[clj-http.client :as client])

(client/${methodString} "${url}" {:content-type :json
                                               :form-params ${paramsString}
                                               :accept :json})
                `;
      } else if (language == Language.GO) {
        code = `
package main

import (
	"fmt"
	"strings"
	"net/http"
	"io/ioutil"
)

func main() {

	url := "${url}"

	payload := strings.NewReader("${paramsString}")

	req, _ := http.NewRequest("${methodString}", url, payload)

	req.Header.Add("accept", "application/json")
	req.Header.Add("content-type", "application/json")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := ioutil.ReadAll(res.Body)

	fmt.Println(res)
	fmt.Println(string(body))

}
                `;
      } else if (language == Language.JAVA) {
        code = `
AsyncHttpClient client = new DefaultAsyncHttpClient();
client.prepare("${methodString}", "${url}")
  .setHeader("accept", "application/json")
  .setHeader("content-type", "application/json")
  .setBody("${paramsString}")
  .execute()
  .toCompletableFuture()
  .thenAccept(System.out::println)
  .join();

client.close();
                `;
      } else if (language == Language.JAVASCRIPT) {
        code = `
import axios from 'axios';

const options = {
  method: '${methodString}',
  url: '${url}',
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
      } else if (language == Language.KOTLIN) {
        code = `
val client = OkHttpClient()

val mediaType = MediaType.parse("application/json")
val body = RequestBody.create(mediaType, "${paramsString}")
val request = Request.Builder()
  .url("${url}")
  .${methodString}(body)
  .addHeader("accept", "application/json")
  .addHeader("content-type", "application/json")
  .build()

val response = client.newCall(request).execute()
                `;
      } else if (language == Language.PYTHON) {
        code = `
import requests

url = "${url}"

payload = ${paramsString}
headers = {
    "accept": "application/json",
    "content-type": "application/json"
}

response = requests.${methodString}(url, json=payload, headers=headers)

print(response.text)
                `;
      } else if (language == Language.R) {
        code = `
library(httr)

url <- "${url}"

payload <- "${paramsString}"

encode <- "json"

response <- VERB("${methodString}", url, body = payload, content_type("application/json"), accept("application/json"), encode = encode)

content(response, "text")
                `;
      } else if (language == Language.SWIFT) {
        code = `
import Foundation

let headers = [
  "accept": "application/json",
  "content-type": "application/json"
]
let parameters = ${paramsString}

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "${url}")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "${methodString}"
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
        code = this.getMdString(code, language);
      }
    }
    return code;
  }
}
