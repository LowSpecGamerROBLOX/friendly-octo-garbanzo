# v0.1

ROBLOX_PATH="/Applications/Roblox.app/Contents/MacOS"

printLogo() {
  echo "██████╗  ██████╗  ██████╗    ███╗   ███╗ █████╗  ██████╗ ██████╗ ███████╗ " 
  echo "██╔══██╗██╔═══██╗██╔════╝    ████╗ ████║██╔══██╗██╔════╝██╔═══██╗██╔════╝ " 
  echo "██████╔╝██║   ██║██║         ██╔████╔██║███████║██║     ██║   ██║███████╗ " 
  echo "██╔══██╗██║   ██║██║         ██║╚██╔╝██║██╔══██║██║     ██║   ██║╚════██║ " 
  echo "██║  ██║╚██████╔╝╚██████╗    ██║ ╚═╝ ██║██║  ██║╚██████╗╚██████╔╝███████║ " 
  echo "╚═╝  ╚═╝ ╚═════╝  ╚═════╝    ╚═╝     ╚═╝╚═╝  ╚═╝ ╚═════╝ ╚═════╝ ╚══════╝ " 
  echo "                                                                          " 
  echo "██╗   ██╗███╗   ██╗ ██████╗ ███████╗███████╗██╗ ██████╗██╗ █████╗ ██╗     " 
  echo "██║   ██║████╗  ██║██╔═══██╗██╔════╝██╔════╝██║██╔════╝██║██╔══██╗██║     " 
  echo "██║   ██║██╔██╗ ██║██║   ██║█████╗  █████╗  ██║██║     ██║███████║██║     " 
  echo "██║   ██║██║╚██╗██║██║   ██║██╔══╝  ██╔══╝  ██║██║     ██║██╔══██║██║     " 
  echo "╚██████╔╝██║ ╚████║╚██████╔╝██║     ██║     ██║╚██████╗██║██║  ██║███████╗"
  echo " ╚═════╝ ╚═╝  ╚═══╝ ╚═════╝ ╚═╝     ╚═╝     ╚═╝ ╚═════╝╚═╝╚═╝  ╚═╝╚══════╝"
  echo "                                                                          "
}

printLogo
echo "Placing ClientAppSettings.json in $ROBLOX_PATH"

if [ -d "$ROBLOX_PATH/ClientSettings"  ]; then
  echo "ClientSettings folder does not exist. creating one"
else
  mkdir "$ROBLOX_PATH/ClientSettings"
fi

cp './ClientAppSettings.json' "$ROBLOX_PATH/ClientSettings/ClientAppSettings.json" 
echo "done"
