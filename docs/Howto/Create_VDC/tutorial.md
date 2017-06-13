
## Repositories

- https://github.com/Jumpscale/ays_jumpscale8
  - Templates: https://github.com/Jumpscale/ays_jumpscale8/tree/8.2.0/templates


## Variables

```
CLIENT_ID="..."
CLIENT_SECRET="..."
BASE_URL="192.168.196.177"
AYS_PORT="5000"
REPO_NAME="yvestest25"
GIT_URL="http://somewhere"
G8_URL="be-g8-4.demo.greenitglobe.com"
LOGIN="api_test_user"
PASSWORD="aysrocks"
ACCOUNT="Demo"
USERNAME="..."
EMAIL="..."
VDC_NAME="testvdc"
LOCATION="be-g8-4"
EXTERNAL_NETWORK="..."

echo "CLIENT_ID: "$CLIENT_ID
echo "CLIENT_SECRET: "$CLIENT_SECRET
echo "BASE_URL: "$BASE_URL
echo "AYS_PORT: "$AYS_PORT
echo "REPO_NAME: "$REPO_NAME
echo "GIT_URL: "$GIT_URL
echo "G8_URL: "$G8_URL
echo "LOGIN: "$LOGIN
echo "PASSWORD: "$PASSWORD
echo "ACCOUNT: "$ACCOUNT
echo "USERNAME: "$USERNAME
echo "EMAIL: "$EMAIL
echo "VDC_NAME: "$VDC_NAME
echo "LOCATION: "$LOCATION
echo "EXTERNAL NETWORK: "$EXTERNAL_NETWORK
```

## CLI



## List all repositories

```bash
BASE_URL="localhost"
AYS_PORT="5000"
curl -X GET \
     -H "Content-Type: application/json" \
     http://$BASE_URL:$AYS_PORT/ays/repository \
     | python -m json.tool
```

## Create new repository

```bash
REPO_NAME="..."
GIT_URL="https://github.com/user/reponame"
curl -X POST \
     -H "Content-Type: application/json" \
     -d '{"name":"'$REPO_NAME'", "git_url":"'$GIT_URL'"}' \
     http://$BASE_URL:$AYS_PORT/ays/repository
```

## Create new g8client service

```bash
G8_URL="be-gen-1.demo.greenitglobe.com"
LOGIN="..."
PASSWORD="..."
ACCOUNT="..."
curl -X POST \
     -v \
     -H "Content-Type: application/json" \
     -d '{"name":"cl.yaml","content":"g8client__cl:\n  url: '$G8_URL'\n  login: '$LOGIN'\n  password: '$PASSWORD'\n  account: '$ACCOUNT'"}' \
     http://$BASE_URL:$AYS_PORT/ays/repository/$REPO_NAME/blueprint
```

As a result the blueprint will be available in the `blueprints` director:
```
vi blueprints/cl.yaml
```

Execute g8client:
```bash
curl -X POST \
     http://$BASE_URL:$AYS_PORT/ays/repository/$REPO_NAME/blueprint/cl.yaml
```

## Create VDC

```bash
LOCATION="be-gen-1"
VDC_NAME="..."

curl -X POST \
     -H "Content-Type: application/json" \
     -d '{"name":"'$VDC_NAME'.yaml","content":"vdc__'$VDC_NAME':\n  g8client: cl\n  location: '$LOCATION'"}' \
     http://$BASE_URL:$AYS_PORT/ays/repository/$REPO_NAME/blueprint
```

Execute:
```bash
curl -X POST \
    http://$BASE_URL:$AYS_PORT/ays/repository/$REPO_NAME/blueprint/$VDC_NAME.yaml
```

## Blueprint for the install actions

```bash
curl -X POST \
     -H "Content-Type: application/json" \
     -d '{"name":"actions.yaml","content":"actions:\n  - action: install\n"}' \
     http://$BASE_URL:$AYS_PORT/ays/repository/$REPO_NAME/blueprint
```

Execute:
```bash
curl -X POST \
     http://$BASE_URL:$AYS_PORT/ays/repository/$REPO_NAME/blueprint/actions.yaml
```

Start a run to actually deploy the VDC:
```bash
curl -X POST \
     http://$BASE_URL:$AYS_PORT/ays/repository/$REPO_NAME/aysrun | python -m json.tool
```

## Grant user access

Optionally, create a new user first:

```bash
USERNAME="..."
EMAIL="..."
curl -X POST \
     -H "Content-Type: application/json" \
     -d '{"name":"'$USERNAME'.yaml","content":"uservdc__'$USERNAME':\n  g8client: cl\n  email: '$EMAIL'\n  provider: itsyouonline"}' \
     http://$BASE_URL:$AYS_PORT/ays/repository/$REPO_NAME/blueprint
```

Execute:
```bash
curl -X POST \
    http://$BASE_URL:$AYS_PORT/ays/repository/$REPO_NAME/blueprint/$USERNAME.yaml
```

New blueprint for VDC to add user:

``` bash
curl -X POST \
     -H "Content-Type: application/json" \
     -d '{"name":"grantaccess.yaml","content":"vdc__'$VDC_NAME':\n  uservdc:\n    - '$USERNAME'"}' \
     http://$BASE_URL:$AYS_PORT/ays/repository/$REPO_NAME/blueprint
```

Execute:
```bash
curl -X POST \
    http://$BASE_URL:$AYS_PORT/ays/repository/$REPO_NAME/blueprint/grantaccess.yaml
```

Start a run to actually pickup the change:
```bash
curl -X POST \
     http://$BASE_URL:$AYS_PORT/ays/repository/$REPO_NAME/aysrun | python -m json.tool
```

## Delete a VDC

...
