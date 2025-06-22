import reflex as rx
import asyncio
from typing import TypedDict, List, Optional, Dict, Any


class Project(TypedDict):
    title: str
    description: str
    technologies: List[str]
    image_url: Optional[str]
    repo_url: Optional[str]
    live_url: Optional[str]


class ProcessedProject(TypedDict):
    title: str
    description: str
    technologies: List[str]
    image_url: Optional[str]
    repo_url: Optional[str]
    live_url: Optional[str]
    display_title: str
    display_description: str
    display_technologies: List[str]


class PortfolioState(rx.State):
    name: str = "Kent Vugs Nielsen"
    bio: str = (
        "Driven Data Scientist & AI Engineer specializing in building impactful machine learning solutions. Passionate about leveraging data to uncover insights and drive innovation. Let's connect!"
    )
    profile_picture_url: str = "/profile.jpeg"
    about_me_summary: str = (
        "I am a results-oriented Data Scientist with expertise in developing and deploying machine learning models, performing in-depth statistical analysis, and creating compelling data visualizations. I excel at bridging the gap between complex data and actionable business strategies. My passion lies in continuous learning and applying cutting-edge AI techniques to solve real-world problems, fostering innovation and efficiency."
    )
    hard_skills: List[str] = [
        "Python (Pandas, NumPy, Scikit-learn, PyTorch)",
        "Advanced SQL & NoSQL (TSQL, Pinecone, MongoDB)",
        "Machine Learning (XGBoost, KNN, Transformers, NLP)",
        "Deep Learning Frameworks (PyTorch)",
        "Data Visualization (Seaborn, Matplotlib, Power BI)",
        "MLOps (Docker, Kubernetes, MLFlow)",
        "Cloud Platforms (Azure)",
        "Big Data Ecosystem (Spark, Hadoop)",
    ]
    soft_skills: List[str] = [
        "Strategic Problem Solving",
        "Advanced Critical Thinking & Analytical Skills",
        "Effective Communication (Technical & Executive audiences)",
        "Cross-functional Collaboration & Leadership",
        "High Adaptability & Growth Mindset",
        "Agile Project Management & Delivery",
    ]
    interests: List[str] = [
        "AI in Algorithmic Trading and FinTech.",
        "Mentoring aspiring data scientists.",
        "Data-driven decision making in business.",
        "Exploring generative AI and its applications.",
        "AI ethics and responsible AI development.",
    ]
    projects: List[Project] = [
        {
            "title": "AI-Powered Predictive Maintenance System for Industrial Equipment",
            "description": "Developed a sophisticated system using sensor data, time-series analysis, and Long Short-Term Memory (LSTM) networks to accurately predict equipment failures in a manufacturing setting. This proactive approach significantly reduced operational downtime by 25% and lowered maintenance costs by 15% through optimized scheduling and resource allocation.",
            "technologies": [
                "Python",
                "TensorFlow/Keras",
                "Pandas",
                "NumPy",
                "Scikit-learn",
                "AWS SageMaker",
                "Grafana",
                "SQL",
            ],
            "image_url": "/project.png",
            "repo_url": "https://github.com/yourusername/predictive-maintenance",
            "live_url": None,
        },
        {
            "title": "Customer Churn Prediction Model with Explainable AI",
            "description": "Built and deployed a high-performance classification model (XGBoost) for a telecom company, identifying at-risk customers with 85% accuracy. Integrated SHAP (SHapley Additive exPlanations) to provide actionable insights into churn drivers, enabling targeted retention campaigns and personalized customer engagement strategies.",
            "technologies": [
                "Python",
                "Scikit-learn",
                "XGBoost",
                "SHAP",
                "Flask",
                "Docker",
                "Plotly Dash",
            ],
            "image_url": "/project_placeholder.png",
            "repo_url": "https://github.com/yourusername/customer-churn-model",
            "live_url": "https://churn-dashboard.example.com",
        },
        {
            "title": "Natural Language Search Engine for Legal Documents",
            "description": "Implemented an advanced semantic search engine using Transformer models (BERT variants) and vector databases (FAISS) for a large corpus of legal documents. This system improved information retrieval speed and relevance by over 5x compared to traditional keyword-based search, significantly enhancing paralegal and attorney productivity.",
            "technologies": [
                "Python",
                "Hugging Face Transformers",
                "PyTorch",
                "FAISS",
                "Elasticsearch",
                "FastAPI",
                "React",
            ],
            "image_url": "/project_placeholder.png",
            "repo_url": "https://github.com/yourusername/semantic-doc-search",
            "live_url": None,
        },
        {
            "title": "Real-time Anomaly Detection in Financial Transactions",
            "description": "Designed and deployed a scalable streaming data pipeline using Apache Kafka and Spark Streaming for real-time anomaly detection in high-volume financial transactions. The system identifies fraudulent patterns and outliers with low latency, preventing significant financial losses.",
            "technologies": [
                "Python",
                "Scala",
                "Apache Spark",
                "Kafka",
                "Cassandra",
                "Prometheus",
                "Grafana",
            ],
            "image_url": "/project_placeholder.png",
            "repo_url": "https://github.com/yourusername/anomaly-detection",
            "live_url": None,
        },
        {
            "title": "Computer Vision for Automated Quality Control in Manufacturing",
            "description": "Developed a Convolutional Neural Network (CNN) based model to automatically detect microscopic defects in manufactured electronic components. The system achieved 99.2% accuracy, outperforming human inspectors and improving production line efficiency and product quality.",
            "technologies": [
                "Python",
                "PyTorch",
                "OpenCV",
                "TensorRT (for deployment)",
                "AWS Rekognition (for PoC)",
                "FastAPI",
                "Docker",
            ],
            "image_url": "/project_placeholder.png",
            "repo_url": "https://github.com/yourusername/cv-quality-control",
            "live_url": "https://qc-demo.example.com",
        },
        {
            "title": "Personalized Recommendation Engine for E-commerce Platform",
            "description": "Created a hybrid recommendation system (collaborative filtering and content-based) for a large e-commerce platform. This engine increased user engagement metrics by 18% and average order value by 12% through tailored product suggestions.",
            "technologies": [
                "Python",
                "SurpriseLib",
                "Spark MLlib",
                "LightFM",
                "Redis",
                "Airflow",
                "AWS Personalize",
            ],
            "image_url": "/project_placeholder.png",
            "repo_url": "https://github.com/yourusername/recommendation-engine",
            "live_url": None,
        },
    ]
    contact_email_address: str = "k.vugs@pm.me"
    linkedin_url: str = "https://linkedin.com/in/vugs"
    github_url: str = "https://github.com/kent1325"
    titles: list[str] = [
        "Mathmatics",
        "Statistics",
        "Programming",
        "Machine Learning",
        "I'M A DATA SCIENTIST",
    ]
    current_title_index: int = 0
    displayed_title_text: str = ""
    _typewriter_running: bool = False
    current_project_index: int = 0
    num_projects_to_display: int = 3
    is_projects_scrolling_paused: bool = False
    auto_scroll_interval: float = 4.0
    _project_scroll_task_started: bool = False
    _carousel_transition_duration_s: float = 1.0
    contact_name: str = ""
    contact_email: str = ""
    contact_message: str = ""
    contact_errors: dict[str, str] = {}
    is_contact_submitting: bool = False
    MAX_CONTACT_MESSAGE_LENGTH: int = 1000
    PROJECT_TITLE_MAX_LENGTH: int = 33
    PROJECT_DESCRIPTION_MAX_LENGTH: int = 120
    PROJECT_TECHNOLOGIES_MAX_DISPLAY: int = 6

    @rx.var
    def contact_message_length(self) -> int:
        return len(self.contact_message)

    @rx.event
    async def handle_contact_submission(self, form_data: dict):
        self.is_contact_submitting = True
        self.contact_errors = {}
        yield
        _contact_name = form_data.get("contact_name", "")
        _contact_email = form_data.get("contact_email", "")
        _contact_message = form_data.get("contact_message", "")
        self.contact_name = _contact_name
        self.contact_email = _contact_email
        self.contact_message = _contact_message
        if not self.contact_name.strip():
            self.contact_errors["name"] = "Full name is required."
        if not self.contact_email.strip():
            self.contact_errors["email"] = "Email address is required."
        elif (
            "@" not in self.contact_email
            or "." not in self.contact_email.split("@")[-1]
        ):
            self.contact_errors["email"] = "Please enter a valid email address."
        if not self.contact_message.strip():
            self.contact_errors["message"] = "Message cannot be empty."
        elif len(self.contact_message) > self.MAX_CONTACT_MESSAGE_LENGTH:
            self.contact_errors["message"] = (
                f"Message is too long (max {self.MAX_CONTACT_MESSAGE_LENGTH} characters)."
            )
        if self.contact_errors:
            self.is_contact_submitting = False
            error_messages = ". ".join(self.contact_errors.values())
            yield rx.toast.error(
                f"Submission failed: {error_messages}",
                duration=4000,
            )
            return

        await asyncio.sleep(1.5)
        self.contact_name = ""
        self.contact_email = ""
        self.contact_message = ""
        self.is_contact_submitting = False
        yield rx.toast.info(
            "Functionality is not implemented yet!",
            duration=5000,
        )
        # yield rx.toast.success(
        #     "Message sent successfully! I'll get back to you soon.",
        #     duration=5000,
        # )

    @rx.event
    def cycle_projects(self, direction: int):
        num_total_projects = len(self.projects)
        if num_total_projects == 0:
            return
        if num_total_projects <= self.num_projects_to_display:
            if self.current_project_index != 0:
                self.current_project_index = 0
            return
        if (
            self.current_project_index
            == num_total_projects - self.num_projects_to_display
        ):
            self.current_project_index = 0
        else:
            self.current_project_index = (
                self.current_project_index + direction + num_total_projects
            ) % num_total_projects

    @rx.var
    def can_cycle_projects(self) -> bool:
        return len(self.projects) > self.num_projects_to_display

    @rx.event(background=True)
    async def typewriter_effect_loop(self):
        async with self:
            if self._typewriter_running:
                return
            self._typewriter_running = True
        if not self.titles:
            async with self:
                self._typewriter_running = False
            return
        while True:
            current_target_title = ""
            _idx = 0
            async with self:
                _idx = self.current_title_index % len(self.titles) if self.titles else 0
            if not self.titles:
                async with self:
                    self._typewriter_running = False
                return
            current_target_title = self.titles[_idx]
            for i in range(len(current_target_title) + 1):
                if _idx != len(self.titles) - 1:
                    async with self:
                        self.displayed_title_text = "I Do " + current_target_title[:i]
                    await asyncio.sleep(0.12)
                else:
                    async with self:
                        self.displayed_title_text = current_target_title[:i]
                    await asyncio.sleep(0.12)
                yield

            if _idx != len(self.titles) - 1:
                await asyncio.sleep(2.0)
            else:
                await asyncio.sleep(5.0)
            for i in range(len(current_target_title), -1, -1):
                if _idx != len(self.titles) - 1:
                    if _idx == len(self.titles) - 2:
                        if i == 0:
                            for j in range(len("I Do "), -1, -1):
                                async with self:
                                    self.displayed_title_text = "I Do "[:j]
                                await asyncio.sleep(0.06)
                        else:
                            async with self:
                                self.displayed_title_text = (
                                    "I Do " + current_target_title[:i]
                                )
                            await asyncio.sleep(0.06)
                    else:
                        async with self:
                            self.displayed_title_text = (
                                "I Do " + current_target_title[:i]
                            )
                        await asyncio.sleep(0.06)
                else:
                    async with self:
                        self.displayed_title_text = current_target_title[:i]
                    await asyncio.sleep(0.06)
                yield
            await asyncio.sleep(0.5)
            async with self:
                self.current_title_index += 1
            yield

    @rx.event
    def pause_project_scrolling(self):
        self.is_projects_scrolling_paused = True

    @rx.event
    def resume_project_scrolling(self):
        self.is_projects_scrolling_paused = False

    @rx.event(background=True)
    async def start_project_auto_scroll(self):
        async with self:
            if self._project_scroll_task_started or not self.can_cycle_projects:
                return
            self._project_scroll_task_started = True
        sleep_duration = max(
            self.auto_scroll_interval,
            self._carousel_transition_duration_s,
        )
        while True:
            await asyncio.sleep(sleep_duration)
            async with self:
                if not self.is_projects_scrolling_paused and self.can_cycle_projects:
                    num_total_projects = len(self.projects)
                    if num_total_projects > 0:
                        if (
                            self.current_project_index
                            == num_total_projects - self.num_projects_to_display
                        ):
                            self.current_project_index = 0
                        else:
                            self.current_project_index = (
                                self.current_project_index + 1
                            ) % num_total_projects
            yield

    @rx.var
    def _item_viewport_width_percentage(self) -> float:
        if self.num_projects_to_display <= 0:
            return 100.0
        return 100.0 / self.num_projects_to_display

    @rx.var
    def renderable_projects(self) -> List[Project]:
        if not self.projects or self.num_projects_to_display <= 0:
            return []
        if len(self.projects) <= self.num_projects_to_display:
            return self.projects
        num_to_append = self.num_projects_to_display
        if num_to_append <= 0:
            num_to_append = 1
        return self.projects + self.projects[:num_to_append]

    @rx.var
    def processed_renderable_projects(
        self,
    ) -> List[ProcessedProject]:
        original_projects = self.renderable_projects
        processed_list: List[ProcessedProject] = []
        for p_data in original_projects:
            title = p_data["title"]
            display_t: str
            if len(title) > self.PROJECT_TITLE_MAX_LENGTH:
                display_t = title[: self.PROJECT_TITLE_MAX_LENGTH - 3] + "..."
            else:
                display_t = title
            description = p_data["description"]
            display_d: str
            if len(description) > self.PROJECT_DESCRIPTION_MAX_LENGTH:
                display_d = (
                    description[: self.PROJECT_DESCRIPTION_MAX_LENGTH - 3] + "..."
                )
            else:
                display_d = description
            technologies = p_data["technologies"]
            display_techs: List[str]
            if len(technologies) > self.PROJECT_TECHNOLOGIES_MAX_DISPLAY:
                display_techs = technologies[: self.PROJECT_TECHNOLOGIES_MAX_DISPLAY]
            else:
                display_techs = technologies
            processed_p: ProcessedProject = {
                "title": p_data["title"],
                "description": p_data["description"],
                "technologies": p_data["technologies"],
                "image_url": p_data["image_url"],
                "repo_url": p_data["repo_url"],
                "live_url": p_data["live_url"],
                "display_title": display_t,
                "display_description": display_d,
                "display_technologies": display_techs,
            }
            processed_list.append(processed_p)
        return processed_list

    @rx.var
    def project_card_style(self) -> dict[str, str]:
        return {"height": "100%", "flex_shrink": "0"}

    @rx.var
    def project_card_base_class_name(self) -> str:
        return "w-full md:w-[calc(50%_-_1rem)] lg:w-[calc(33.3333%_-_1.3333rem)]"

    @rx.var
    def carousel_track_style(self) -> dict[str, str]:
        track_total_width_perc_str = "100"
        num_renderable = len(self.processed_renderable_projects)
        if num_renderable > 0 and self.num_projects_to_display > 0:
            track_total_width_perc = (
                num_renderable / self.num_projects_to_display * 100.0
            )
            track_total_width_perc_str = f"{track_total_width_perc:.4f}"
        translate_percentage_val = 0.0
        if num_renderable > 0:
            translate_percentage_val = self.current_project_index * (
                100.0 / num_renderable
            )
        translate_percentage_val_str = f"{translate_percentage_val:.4f}"
        return {
            "display": "flex",
            "transition": f"transform {self._carousel_transition_duration_s}s ease-in-out",
            "transform": f"translateX(-{translate_percentage_val_str}%)",
            "width": f"{track_total_width_perc_str}%",
            "will_change": "transform",
        }
