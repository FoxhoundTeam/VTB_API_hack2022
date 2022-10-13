from typing import Optional, Union

from fastapi import FastAPI, Header

from common.factories import create_factory_class

from .models import Oauth2Error, Oauth2TokenRequest, Oauth2TokenResponse, ResponseType2, UserInfo

app = FastAPI(
    title="VTB ID  Authorization server (Хакатон)",
    description="## Авторизация приложений OAuth\n***\nVTB ID — сервер авторизации OAuth2, который поддерживает тип авторизации authorization code.\n\nДля настройки авторизации OAuth2-приложений, запущенных в web-браузере, используется процесс авторизации web2web.\n\n## Авторизация и получение userinfo\n***\n* Авторизация приложения и аутентификация пользователя\n\n   Пользователь открывает страницу сервера авторизации для аутентификации пользователя при переходе по ссылке (например, [https://id.vtb.ru/oauth2/authorize?client_id=123123&response_type=code&state=fhweijgfhrewh&redirect_uri=http://partner.ru/login&scope=name+surname]()).   \n   После успешной аутентификации сервер авторизации перенаправляет пользователя в приложение с передачей кода авторизации (ссылка вида [https://partner.ru/login?code=fjfghguhregurh&state=fhweijgfhrewh]()).   \n   Если при авторизации произошла какая-то ошибка, сервер авторизации перенаправит пользователя в приложение с ошибкой (ссылка вида [https: //partner.ru/login?error=access_denied&state=fhweijgfhrewh]())\n\n- Получение токенов доступа\n\n   Приложение, используя код авторизации, Сlient Id и Сlient Secret, обращается к серверу авторизации для  получения токенов доступа (запрос на /oauth2/token). Код авторизации можно использовать только ОДИН раз.\n\n- Получение персональных данных\n\n   Приложение,  имея токены доступа, может выполнять запросы на получение персональных данных пользователя (запрос на /oauth2/me). Получить можно лишь те данные, которые были запрошены на этапе авторизации (scope-параметр).\n",
    contact={},
    version="1.0.1",
    # servers=[{"url": "https://epa.api.vtb.ru/openapi/hackathon/id.vtb.ru"}],
)


@app.get("/oauth2/authorize", response_model=None)
def authorizationendpoint(
    redirect_uri: str,
    authorization: Optional[str] = Header("Bearer {token}", alias="Authorization"),
    scope: Optional[str] = None,
    state: str = ...,
    client_id: str = ...,
    response_type: ResponseType2 = ...,
) -> None:
    """
    Authorization endpoint
    """
    pass


@app.get(
    "/oauth2/me",
    response_model=UserInfo,
    responses={"400": {"model": Oauth2Error}, "500": {"model": Oauth2Error}},
)
def user_infoendpoint(
    authorization: Optional[str] = Header("Bearer {token}", alias="Authorization"),
    scopes: Optional[str] = None,
) -> Union[UserInfo, Oauth2Error]:
    """
    UserInfo endpoint
    """
    return create_factory_class(UserInfo).build()


@app.post(
    "/oauth2/token",
    response_model=Oauth2TokenResponse,
    responses={
        "400": {"model": Oauth2Error},
        "401": {"model": Oauth2Error},
        "500": {"model": Oauth2Error},
    },
)
def tokenendpoint(
    authorization: Optional[str] = Header("Bearer {token}", alias="Authorization"),
    body: Oauth2TokenRequest = None,
) -> Union[Oauth2TokenResponse, Oauth2Error]:
    """
    Token endpoint
    """
    return create_factory_class(Oauth2TokenResponse).build()


@app.get("/oidc/logout", response_model=None)
def logoutendpoint(authorization: Optional[str] = Header("Bearer {token}", alias="Authorization")) -> None:
    """
    Logout endpoint
    """
    pass
