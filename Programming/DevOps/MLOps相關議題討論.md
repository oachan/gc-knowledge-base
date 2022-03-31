# DataOps、MLOps、AIOps

- [DataOps、MLOps 和 AIOps，你要的是哪個 Ops？](https://www.youmelive.com/keji/code/372507.html)
- [What the Ops are you talking about?](https://towardsdatascience.com/what-the-ops-are-you-talking-about-518b1b1a2694)

* DevOps 更快地交付軟體
* DataOps 更快地交付數據
* MLOps 更快地交付機器學習模型
* 附加：AIOps 利用 AI 的功能增強了 DevOps 工具
> AIOps 平臺利用大數據、現代機器學習以及其他先進的分析技術，直接或間接地增強 IT 運維（監控、自動化和服務臺），具有前瞻性、個性化以及動態的洞察力。

# AI 自動平台化技術: 系統軟體架構
* 平台
    * Public Cloud: GCP、AWS
        * 公用雲是第三方提供一般公眾或大型產業集體使用的雲端基礎設施，擁有它的組織出售雲端服務，系統服務提供者藉由租借方式提供客戶有能力部署及使用雲端服務。
    * On Premise: K8S
        *  內部部署軟件是在使用該軟件的個人或組織內部的計算機上安裝並運行的，而不是在服務器場或云等遠程設施中運行。Cloud Storage、Persistent Disk、Pub/Sub、Stack Driver、Cloud SQL、Load Balancer 都會需要有替代方案。
* 網路
  * Overlay Network: Kubernetes - Container Network Interface 
    * 1. 提供 Pod 上網能力，通常都會希望能夠有連接外網的能力 2. 分配 IP 地址，幫每個 Pod 找一個獨立不重複的 IP，至於是 ipv4 或是 ipv6 都可以。從 kubernetes 1.16 開始支援 ipv6 之後對於使用 ipv6 的Pod 再管理上會顯得相對容易 3. 幫忙實現 Network Policy， kubernetes 內部有 Network Policy 去限制 Pod 與 Pod 之間的網路傳輸，然而 kubernetes 本身只有定義介面，仰賴各個 CNI 去完成。
    * https://draveness.me/whys-the-design-overlay-network/
    * https://ithelp.ithome.com.tw/articles/10220626
  * Load Balancer
  * Ingress Controller
* 儲存
  * Block Storage: Longhorn, GlusterFS
    * https://zhuanlan.zhihu.com/p/337076325
  * Service Mesh: Istio, traefik 
    * https://medium.com/brobridge/%E6%98%8F%E5%80%92-service-mesh-%E5%8E%9F%E4%BE%86%E4%B8%8D%E6%98%AF%E7%B6%B2%E6%A0%BC%E6%9C%8D%E5%8B%99-9a4b0636371f
  * Workflow Scheduler: Celery, KEDA 
  * Register: Data / Model version  dvc?、GCP Container Registry: (Main Repo, Env. Repo., Infrastructure-as-code)
    * Data / Model version  dvc?
    * Coontainer Image的存放區，用以儲存與管理 Images
    * https://cloud.google.com/container-registry?hl=zh-tw
  * Serverless Framework(GKE): Google Cloud Run (Knative)
    * Google Cloud Run是基於開源之 Knative 而提供之服務
  * Serverless Framework(On Premise): Knative?
    * 1. 最初是由 Google 與 50 多間公司攜手合作建立而成
    * 2. Knative 為 Kubernetes 上的雲端原生應用程式提供了將資源調度率降至零、自動調度資源、叢集內建構和事件架構等功能。 
    * 3. Focused API with higher level abstractions for common app use-cases.
    * 4. Stand up a scalable, secure, stateless service in seconds.
    * 5. Loosely coupled features let you use the pieces you need.
    * 6. Pluggable components let you bring your own logging and monitoring, networking, and service mesh.
    * 7. Knative is portable: run it anywhere Kubernetes runs, never worry about vendor lock-in.
    * 8. Idiomatic developer experience, supporting common patterns such as GitOps, DockerOps, ManualOps.
    * 9. Knative can be used with common tools and frameworks such as Django, Ruby on Rails, Spring, and many more.
    * https://cloud.google.com/knative?hl=zh-tw
    * https://knative.dev/
* 偵測
  * Metric Montor: kube-state-metrics, metrics-server, metricbeat
    * kube-state-metrics : 
    * metrics-server :
    * metricbeat：Elastic Beats  中針對主機狀態監測的指標工具，整合包含一般主機、Docker、Kubernetes 模塊
    * https://github.com/kubernetes/kube-state-metrics
    * https://github.com/kubernetes-sigs/metrics-server
    * https://www.elastic.co/cn/beats/metricbeat
  * Log Monitor: On Premise：Logstash, filebeat, fluent, Kibana、GKE：stackdriver + (Kibana?)
  * AlertManager: On Premise：Kibana Alerting、GKE：(Kibana Alerting?)
* 開發
  * Administrator Console: Kubeflow
    * 建立專案，分配計算資源、資源使用度監控
  * Developer Console: Papermill
    * 資料處理、標註、訓練/測試資料集管理、AutoML導入前資料格式轉換、模型建模管理、模型部署
    * https://netflixtechblog.com/scheduling-notebooks-348e6c14cfd6
* 部屬
  * GitOps
    * 異質性雲端持續部署
    * https://www.hwchiu.com/gitops.html
    * https://medium.com/starbugs/gitops-%E9%80%8F%E9%81%8E-argo-cd-%E8%AA%8D%E8%AD%98-gitops-f0a596764fdd

# AI 自動平台化技術: Infra
* 平台基礎架構
  * Kubernetes / Docker
  * Unified Log
  * Data / Model Repository
  * Default Image Providing
  * Image Builder
  * Data as a Service
  * 平台部署
* Orchestration
  * 開發環境 Resource Provisioning
  * 開發環境 Usage Monitoring
* Pipeline Control
  * 系統中 Pipeline 架構設計
  * pipeline control
* Deployment
  * 資料、程式碼、模型、環境參數版控
  * 資料、程式碼、模型應用部署
* (internal) SIT
  * 平台開發的CI/CD
  * system Integration Test

# 機器學習項目相關的資源：
- [Awesome Machine Learning](https://github.com/josephmisiti/awesome-machine-learning)
- [Awesome production machine learning](https://github.com/ethicalml/awesome-production-machine-learning)
- [awesome-AIOps](https://github.com/linjinjin123/awesome-AIOps)

## 相關工具
- [papermill](https://papermill.readthedocs.io/en/latest/)
- [DVC](https://dvc.org/)

