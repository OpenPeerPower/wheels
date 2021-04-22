# Open Peer Power Wheels builder

```sh

$ python3 -m builder \
    --apk build-base \
    --index https://OpenPeerPower/whl-ix \
    --requirement requirements_all.txt \
    --remote user@server:/wheels
```

## Supported file transfer

- rsync

## Folder structure of index folder:

`/alpine-{version}/{arch}/*`
