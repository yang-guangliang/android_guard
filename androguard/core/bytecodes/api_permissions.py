DVM_PERMISSIONS_BY_PERMISSION = {
    "BIND_DEVICE_ADMIN": {
        "Landroid/app/admin/DeviceAdminReceiver;": [
            ("C", "ACTION_DEVICE_ADMIN_ENABLED", "Ljava/lang/String;"),
        ],
        "Landroid/app/admin/DevicePolicyManager;": [
            ("F", "getRemoveWarning",
             "(Landroid/content/ComponentName; Landroid/os/RemoteCallback;)"),
            ("F", "reportFailedPasswordAttempt", "()"),
            ("F", "reportSuccessfulPasswordAttempt", "()"),
            ("F", "setActiveAdmin", "(Landroid/content/ComponentName;)"),
            ("F", "setActivePasswordState", "(I I)"),
        ],
        "Landroid/app/admin/IDevicePolicyManager$Stub$Proxy;": [
            ("F", "getRemoveWarning",
             "(Landroid/content/ComponentName; Landroid/os/RemoteCallback;)"),
            ("F", "reportFailedPasswordAttempt", "()"),
            ("F", "reportSuccessfulPasswordAttempt", "()"),
            ("F", "setActiveAdmin", "(Landroid/content/ComponentName;)"),
            ("F", "setActivePasswordState", "(I I)"),
        ],
    },
    "READ_SYNC_SETTINGS": {
        "Landroid/app/ContextImpl$ApplicationContentResolver;": [
            ("F", "getIsSyncable",
             "(Landroid/accounts/Account; Ljava/lang/String;)"),
            ("F", "getMasterSyncAutomatically", "()"),
            ("F", "getPeriodicSyncs",
             "(Landroid/accounts/Account; Ljava/lang/String;)"),
            ("F", "getSyncAutomatically",
             "(Landroid/accounts/Account; Ljava/lang/String;)"),
        ],
        "Landroid/content/ContentService;": [
            ("F", "getIsSyncable",
             "(Landroid/accounts/Account; Ljava/lang/String;)"),
            ("F", "getMasterSyncAutomatically", "()"),
            ("F", "getPeriodicSyncs",
             "(Landroid/accounts/Account; Ljava/lang/String;)"),
            ("F", "getSyncAutomatically",
             "(Landroid/accounts/Account; Ljava/lang/String;)"),
        ],
        "Landroid/content/ContentResolver;": [
            ("F", "getIsSyncable",
             "(Landroid/accounts/Account; Ljava/lang/String;)"),
            ("F", "getMasterSyncAutomatically", "()"),
            ("F", "getPeriodicSyncs",
             "(Landroid/accounts/Account; Ljava/lang/String;)"),
            ("F", "getSyncAutomatically",
             "(Landroid/accounts/Account; Ljava/lang/String;)"),
        ],
        "Landroid/content/IContentService$Stub$Proxy;": [
            ("F", "getIsSyncable",
             "(Landroid/accounts/Account; Ljava/lang/String;)"),
            ("F", "getMasterSyncAutomatically", "()"),
            ("F", "getPeriodicSyncs",
             "(Landroid/accounts/Account; Ljava/lang/String;)"),
            ("F", "getSyncAutomatically",
             "(Landroid/accounts/Account; Ljava/lang/String;)"),
        ],
    },
    "FACTORY_TEST": {
        "Landroid/content/pm/ApplicationInfo;": [
            ("C", "FLAG_FACTORY_TEST", "I"),
            ("C", "flags", "I"),
        ],
        "Landroid/content/Intent;": [
            ("C", "IntentResolution", "Ljava/lang/String;"),
            ("C", "ACTION_FACTORY_TEST", "Ljava/lang/String;"),
        ],
    },
    "SET_ALWAYS_FINISH": {
        "Landroid/app/IActivityManager$Stub$Proxy;": [
            ("F", "setAlwaysFinish", "(B)"),
        ],
    },
    "READ_CALENDAR": {
        "Landroid/provider/Calendar$CalendarAlerts;": [
            ("F", "alarmExists", "(Landroid/content/ContentResolver; J J J)"),
            ("F", "findNextAlarmTime", "(Landroid/content/ContentResolver; J)"),
            ("F", "query",
             "(Landroid/content/ContentResolver; [L[Ljava/lang/Strin; Ljava/lang/String; [L[Ljava/lang/Strin; Ljava/lang/String;)"
  ),
        ],
        "Landroid/provider/Calendar$Calendars;": [
            ("F", "query",
             "(Landroid/content/ContentResolver; [L[Ljava/lang/Strin; Ljava/lang/String; Ljava/lang/String;)"
  ),
        ],
        "Landroid/provider/Calendar$Events;": [
            ("F", "query",
             "(Landroid/content/ContentResolver; [L[Ljava/lang/Strin; Ljava/lang/String; Ljava/lang/String;)"
  ),
            ("F", "query",
             "(Landroid/content/ContentResolver; [L[Ljava/lang/Strin;)"),
        ],
        "Landroid/provider/Calendar$Instances;": [
            ("F", "query",
             "(Landroid/content/ContentResolver; [L[Ljava/lang/Strin; J J Ljava/lang/String; Ljava/lang/String;)"
  ),
            ("F", "query",
             "(Landroid/content/ContentResolver; [L[Ljava/lang/Strin; J J)"),
        ],
        "Landroid/provider/Calendar$EventDays;": [
            ("F", "query", "(Landroid/content/ContentResolver; I I)"),
        ],
    },
    "ACCESS_DRM": {
        "Landroid/provider/DrmStore;": [
            ("F", "enforceAccessDrmPermission", "(Landroid/content/Context;)"),
        ],
    },
    "CHANGE_CONFIGURATION": {
        "Landroid/app/IActivityManager$Stub$Proxy;": [
            ("F", "updateConfiguration", "(Landroid/content/res/Configuration;)"
  ),
        ],
    },
    "SET_ACTIVITY_WATCHER": {
        "Landroid/app/IActivityManager$Stub$Proxy;": [
            ("F", "profileControl",
             "(Ljava/lang/String; B Ljava/lang/String; Landroid/os/ParcelFileDescriptor;)"
  ),
            ("F", "setActivityController", "(Landroid/app/IActivityController;)"
  ),
        ],
    },
    "GET_PACKAGE_SIZE": {
        "Landroid/app/ContextImpl$ApplicationPackageManager;": [
            ("F", "getPackageSizeInfo",
             "(Ljava/lang/String; LIPackageStatsObserver;)"),
            ("F", "getPackageSizeInfo",
             "(Ljava/lang/String; Landroid/content/pm/IPackageStatsObserver;)"),
        ],
        "Landroid/content/pm/PackageManager;": [
            ("F", "getPackageSizeInfo",
             "(Ljava/lang/String; Landroid/content/pm/IPackageStatsObserver;)"),
        ],
    },
    "CONTROL_LOCATION_UPDATES": {
        "Landroid/telephony/TelephonyManager;": [
            ("F", "disableLocationUpdates", "()"),
            ("F", "enableLocationUpdates", "()"),
        ],
        "Lcom/android/internal/telephony/ITelephony$Stub$Proxy;": [
            ("F", "disableLocationUpdates", "()"),
            ("F", "enableLocationUpdates", "()"),
        ],
    },
    "CLEAR_APP_CACHE": {
        "Landroid/app/ContextImpl$ApplicationPackageManager;": [
            ("F", "freeStorage", "(J LIntentSender;)"),
            ("F", "freeStorageAndNotify", "(J LIPackageDataObserver;)"),
            ("F", "freeStorage", "(J Landroid/content/IntentSender;)"),
            ("F", "freeStorageAndNotify",
             "(J Landroid/content/pm/IPackageDataObserver;)"),
        ],
        "Landroid/content/pm/PackageManager;": [
            ("F", "freeStorage", "(J Landroid/content/IntentSender;)"),
            ("F", "freeStorageAndNotify",
             "(J Landroid/content/pm/IPackageDataObserver;)"),
        ],
        "Landroid/content/pm/IPackageManager$Stub$Proxy;": [
            ("F", "freeStorage", "(J Landroid/content/IntentSender;)"),
            ("F", "freeStorageAndNotify",
             "(J Landroid/content/pm/IPackageDataObserver;)"),
        ],
    },
    "BIND_INPUT_METHOD": {
        "Landroid/view/inputmethod/InputMethod;": [
            ("C", "SERVICE_INTERFACE", "Ljava/lang/String;"),
        ],
    },
    "SIGNAL_PERSISTENT_PROCESSES": {
        "Landroid/app/IActivityManager$Stub$Proxy;": [
            ("F", "signalPersistentProcesses", "(I)"),
        ],
    },
    "BATTERY_STATS": {
        "Lcom/android/internal/app/IBatteryStats$Stub$Proxy;": [
            ("F", "getAwakeTimeBattery", "()"),
            ("F", "getAwakeTimePlugged", "()"),
            ("F", "getStatistics", "()"),
        ],
    },
    "AUTHENTICATE_ACCOUNTS": {
        "Landroid/accounts/AccountManager;": [
            ("F", "addAccountExplicitly",
             "(Landroid/accounts/Account; Ljava/lang/String; Landroid/os/Bundle;)"
  ),
            ("F", "getPassword", "(Landroid/accounts/Account;)"),
            ("F", "getUserData",
             "(Landroid/accounts/Account; Ljava/lang/String;)"),
            ("F", "peekAuthToken",
             "(Landroid/accounts/Account; Ljava/lang/String;)"),
            ("F", "setAuthToken",
             "(Landroid/accounts/Account; Ljava/lang/String; Ljava/lang/String;)"
  ),
            ("F", "setPassword",
             "(Landroid/accounts/Account; Ljava/lang/String;)"),
            ("F", "setUserData",
             "(Landroid/accounts/Account; Ljava/lang/String; Ljava/lang/String;)"
  ),
            ("F", "addAccountExplicitly",
             "(Landroid/accounts/Account; Ljava/lang/String; Landroid/os/Bundle;)"
  ),
            ("F", "getPassword", "(Landroid/accounts/Account;)"),
            ("F", "getUserData",
             "(Landroid/accounts/Account; Ljava/lang/String;)"),
            ("F", "peekAuthToken",
             "(Landroid/accounts/Account; Ljava/lang/String;)"),
            ("F", "setAuthToken",
             "(Landroid/accounts/Account; Ljava/lang/String; Ljava/lang/String;)"
  ),
            ("F", "setPassword",
             "(Landroid/accounts/Account; Ljava/lang/String;)"),
            ("F", "setUserData",
             "(Landroid/accounts/Account; Ljava/lang/String; Ljava/lang/String;)"
  ),
        ],
        "Landroid/accounts/AccountManagerService;": [
            ("F", "addAccount",
             "(Landroid/accounts/Account; Ljava/lang/String; Landroid/os/Bundle;)"
  ),
            ("F", "checkAuthenticateAccountsPermission",
             "(Landroid/accounts/Account;)"),
            ("F", "getPassword", "(Landroid/accounts/Account;)"),
            ("F", "getUserData",
             "(Landroid/accounts/Account; Ljava/lang/String;)"),
            ("F", "peekAuthToken",
             "(Landroid/accounts/Account; Ljava/lang/String;)"),
            ("F", "setAuthToken",
             "(Landroid/accounts/Account; Ljava/lang/String; Ljava/lang/String;)"
  ),
            ("F", "setPassword",
             "(Landroid/accounts/Account; Ljava/lang/String;)"),
            ("F", "setUserData",
             "(Landroid/accounts/Account; Ljava/lang/String; Ljava/lang/String;)"
  ),
        ],
        "Landroid/accounts/IAccountManager$Stub$Proxy;": [
            ("F", "addAccount",
             "(Landroid/accounts/Account; Ljava/lang/String; Landroid/os/Bundle;)"
  ),
            ("F", "getPassword", "(Landroid/accounts/Account;)"),
            ("F", "getUserData",
             "(Landroid/accounts/Account; Ljava/lang/String;)"),
            ("F", "peekAuthToken",
             "(Landroid/accounts/Account; Ljava/lang/String;)"),
            ("F", "setAuthToken",
             "(Landroid/accounts/Account; Ljava/lang/String; Ljava/lang/String;)"
  ),
            ("F", "setPassword",
             "(Landroid/accounts/Account; Ljava/lang/String;)"),
            ("F", "setUserData",
             "(Landroid/accounts/Account; Ljava/lang/String; Ljava/lang/String;)"
  ),
        ],
    },
    "CHANGE_BACKGROUND_DATA_SETTING": {
        "Landroid/net/IConnectivityManager$Stub$Proxy;": [
            ("F", "setBackgroundDataSetting", "(B)"),
        ],
        "Landroid/net/ConnectivityManager;": [
            ("F", "setBackgroundDataSetting", "(B)"),
        ],
    },
    "RESTART_PACKAGES": {
        "Landroid/app/ActivityManagerNative;": [
            ("F", "killBackgroundProcesses", "(Ljava/lang/String;)"),
            ("F", "restartPackage", "(Ljava/lang/String;)"),
        ],
        "Landroid/app/ActivityManager;": [
            ("F", "killBackgroundProcesses", "(Ljava/lang/String;)"),
            ("F", "restartPackage", "(Ljava/lang/String;)"),
        ],
    },
    "CALL_PRIVILEGED": {
        "Landroid/telephony/TelephonyManager;": [
            ("F", "getCompleteVoiceMailNumber", "()"),
        ],
        "Landroid/telephony/PhoneNumberUtils;": [
            ("F", "getNumberFromIntent",
             "(Landroid/content/Intent; Landroid/content/Context;)"),
        ],
    },
    "SET_WALLPAPER_COMPONENT": {
        "Landroid/app/IWallpaperManager$Stub$Proxy;": [
            ("F", "setWallpaperComponent", "(Landroid/content/ComponentName;)"),
        ],
    },
    "DISABLE_KEYGUARD": {
        "Landroid/view/IWindowManager$Stub$Proxy;": [
            ("F", "disableKeyguard", "(Landroid/os/IBinder; Ljava/lang/String;)"
  ),
            ("F", "exitKeyguardSecurely",
             "(Landroid/view/IOnKeyguardExitResult;)"),
            ("F", "reenableKeyguard", "(Landroid/os/IBinder;)"),
        ],
        "Landroid/app/KeyguardManager;": [
            ("F", "exitKeyguardSecurely",
             "(Landroid/app/KeyguardManager$OnKeyguardExitResult;)"),
        ],
        "Landroid/app/KeyguardManager$KeyguardLock;": [
            ("F", "disableKeyguard", "()"),
            ("F", "reenableKeyguard", "()"),
        ],
    },
    "DELETE_PACKAGES": {
        "Landroid/app/ContextImpl$ApplicationPackageManager;": [
            ("F", "deletePackage",
             "(Ljava/lang/String; LIPackageDeleteObserver; I)"),
            ("F", "deletePackage",
             "(Ljava/lang/String; LIPackageDeleteObserver; I)"),
        ],
        "Landroid/content/pm/PackageManager;": [
            ("F", "deletePackage",
             "(Ljava/lang/String; LIPackageDeleteObserver; I)"),
        ],
        "Landroid/content/pm/IPackageManager$Stub$Proxy;": [
            ("F", "deletePackage",
             "(Ljava/lang/String; Landroid/content/pm/IPackageDeleteObserver; I)"
  ),
        ],
    },
    "CHANGE_COMPONENT_ENABLED_STATE": {
        "Landroid/app/ContextImpl$ApplicationPackageManager;": [
            ("F", "setApplicationEnabledSetting", "(Ljava/lang/String; I I)"),
            ("F", "setComponentEnabledSetting", "(LComponentName; I I)"),
            ("F", "setApplicationEnabledSetting", "(Ljava/lang/String; I I)"),
            ("F", "setComponentEnabledSetting",
             "(Landroid/content/ComponentName; I I)"),
        ],
        "Landroid/content/pm/PackageManager;": [
            ("F", "setApplicationEnabledSetting", "(Ljava/lang/String; I I)"),
            ("F", "setComponentEnabledSetting",
             "(Landroid/content/ComponentName; I I)"),
        ],
        "Landroid/content/pm/IPackageManager$Stub$Proxy;": [
            ("F", "setApplicationEnabledSetting", "(Ljava/lang/String; I I)"),
            ("F", "setComponentEnabledSetting",
             "(Landroid/content/ComponentName; I I)"),
        ],
    },
    "ASEC_ACCESS": {
        "Landroid/os/storage/IMountService$Stub$Proxy;": [
            ("F", "getSecureContainerList", "()"),
            ("F", "getSecureContainerPath", "(Ljava/lang/String;)"),
            ("F", "isSecureContainerMounted", "(Ljava/lang/String;)"),
        ],
    },
    "UPDATE_DEVICE_STATS": {
        "Lcom/android/internal/app/IUsageStats$Stub$Proxy;": [
            ("F", "noteLaunchTime", "(LComponentName;)"),
        ],
    },
    "RECORD_AUDIO": {
        "Landroid/net/sip/SipAudioCall;": [
            ("F", "startAudio", "()"),
        ],
        "Landroid/media/MediaRecorder;": [
            ("F", "setAudioSource", "(I)"),
        ],
        "Landroid/speech/SpeechRecognizer;": [
            ("F", "cancel", "()"),
            ("F", "handleCancelMessage", "()"),
            ("F", "handleStartListening", "(Landroid/content/Intent;)"),
            ("F", "handleStopMessage", "()"),
            ("F", "startListening", "(Landroid/content/Intent;)"),
            ("F", "stopListening", "()"),
        ],
        "Landroid/media/AudioRecord;": [
            ("F", "<init>", "(I I I I I)"),
        ],
    },
    "ACCESS_MOCK_LOCATION": {
        "Landroid/location/LocationManager;": [
            ("F", "addTestProvider", "(Ljava/lang/String; B B B B B B B I I)"),
            ("F", "clearTestProviderEnabled", "(Ljava/lang/String;)"),
            ("F", "clearTestProviderLocation", "(Ljava/lang/String;)"),
            ("F", "clearTestProviderStatus", "(Ljava/lang/String;)"),
            ("F", "removeTestProvider", "(Ljava/lang/String;)"),
            ("F", "setTestProviderEnabled", "(Ljava/lang/String; B)"),
            ("F", "setTestProviderLocation",
             "(Ljava/lang/String; Landroid/location/Location;)"),
            ("F", "setTestProviderStatus",
             "(Ljava/lang/String; I Landroid/os/Bundle; J)"),
            ("F", "addTestProvider", "(Ljava/lang/String; B B B B B B B I I)"),
            ("F", "clearTestProviderEnabled", "(Ljava/lang/String;)"),
            ("F", "clearTestProviderLocation", "(Ljava/lang/String;)"),
            ("F", "clearTestProviderStatus", "(Ljava/lang/String;)"),
            ("F", "removeTestProvider", "(Ljava/lang/String;)"),
            ("F", "setTestProviderEnabled", "(Ljava/lang/String; B)"),
            ("F", "setTestProviderLocation",
             "(Ljava/lang/String; Landroid/location/Location;)"),
            ("F", "setTestProviderStatus",
             "(Ljava/lang/String; I Landroid/os/Bundle; J)"),
        ],
        "Landroid/location/ILocationManager$Stub$Proxy;": [
            ("F", "addTestProvider", "(Ljava/lang/String; B B B B B B B I I)"),
            ("F", "clearTestProviderEnabled", "(Ljava/lang/String;)"),
            ("F", "clearTestProviderLocation", "(Ljava/lang/String;)"),
            ("F", "clearTestProviderStatus", "(Ljava/lang/String;)"),
            ("F", "removeTestProvider", "(Ljava/lang/String;)"),
            ("F", "setTestProviderEnabled", "(Ljava/lang/String; B)"),
            ("F", "setTestProviderLocation",
             "(Ljava/lang/String; Landroid/location/Location;)"),
            ("F", "setTestProviderStatus",
             "(Ljava/lang/String; I Landroid/os/Bundle; J)"),
        ],
    },
    "VIBRATE": {
        "Landroid/media/AudioManager;": [
            ("C", "EXTRA_RINGER_MODE", "Ljava/lang/String;"),
            ("C", "EXTRA_VIBRATE_SETTING", "Ljava/lang/String;"),
            ("C", "EXTRA_VIBRATE_TYPE", "Ljava/lang/String;"),
            ("C", "FLAG_REMOVE_SOUND_AND_VIBRATE", "I"),
            ("C", "FLAG_VIBRATE", "I"),
            ("C", "RINGER_MODE_VIBRATE", "I"),
            ("C", "VIBRATE_SETTING_CHANGED_ACTION", "Ljava/lang/String;"),
            ("C", "VIBRATE_SETTING_OFF", "I"),
            ("C", "VIBRATE_SETTING_ON", "I"),
            ("C", "VIBRATE_SETTING_ONLY_SILENT", "I"),
            ("C", "VIBRATE_TYPE_NOTIFICATION", "I"),
            ("C", "VIBRATE_TYPE_RINGER", "I"),
            ("F", "getRingerMode", "()"),
            ("F", "getVibrateSetting", "(I)"),
            ("F", "setRingerMode", "(I)"),
            ("F", "setVibrateSetting", "(I I)"),
            ("F", "shouldVibrate", "(I)"),
        ],
        "Landroid/os/Vibrator;": [
            ("F", "cancel", "()"),
            ("F", "vibrate", "([L; I)"),
            ("F", "vibrate", "(J)"),
        ],
        "Landroid/provider/Settings/System;": [
            ("C", "VIBRATE_ON", "Ljava/lang/String;"),
        ],
        "Landroid/app/NotificationManager;": [
            ("F", "notify", "(I Landroid/app/Notification;)"),
            ("F", "notify", "(Ljava/lang/String; I Landroid/app/Notification;)"
  ),
        ],
        "Landroid/app/Notification/Builder;": [
            ("F", "setDefaults", "(I)"),
        ],
        "Landroid/os/IVibratorService$Stub$Proxy;": [
            ("F", "cancelVibrate", "(Landroid/os/IBinder;)"),
            ("F", "vibrate", "(J Landroid/os/IBinder;)"),
            ("F", "vibratePattern", "([L; I Landroid/os/IBinder;)"),
        ],
        "Landroid/app/Notification;": [
            ("C", "DEFAULT_VIBRATE", "I"),
            ("C", "defaults", "I"),
        ],
    },
    "ASEC_CREATE": {
        "Landroid/os/storage/IMountService$Stub$Proxy;": [
            ("F", "createSecureContainer",
             "(Ljava/lang/String; I Ljava/lang/String; Ljava/lang/String; I)"),
            ("F", "finalizeSecureContainer", "(Ljava/lang/String;)"),
        ],
    },
    "WRITE_SECURE_SETTINGS": {
        "Landroid/bluetooth/BluetoothAdapter;": [
            ("F", "setScanMode", "(I I)"),
            ("F", "setScanMode", "(I)"),
        ],
        "Landroid/server/BluetoothService;": [
            ("F", "setScanMode", "(I I)"),
        ],
        "Landroid/os/IPowerManager$Stub$Proxy;": [
            ("F", "setMaximumScreenOffTimeount", "(I)"),
        ],
        "Landroid/content/pm/IPackageManager$Stub$Proxy;": [
            ("F", "setInstallLocation", "(I)"),
        ],
        "Landroid/bluetooth/IBluetooth$Stub$Proxy;": [
            ("F", "setScanMode", "(I I)"),
        ],
    },
    "SET_ORIENTATION": {
        "Landroid/view/IWindowManager$Stub$Proxy;": [
            ("F", "setRotation", "(I B I)"),
        ],
    },
    "PACKAGE_USAGE_STATS": {
        "Lcom/android/internal/app/IUsageStats$Stub$Proxy;": [
            ("F", "getAllPkgUsageStats", "()"),
            ("F", "getPkgUsageStats", "(LComponentName;)"),
        ],
    },
    "FLASHLIGHT": {
        "Landroid/os/IHardwareService$Stub$Proxy;": [
            ("F", "setFlashlightEnabled", "(B)"),
        ],
    },
    "GLOBAL_SEARCH": {
        "Landroid/app/SearchManager;": [
            ("C", "EXTRA_SELECT_QUERY", "Ljava/lang/String;"),
            ("C", "INTENT_ACTION_GLOBAL_SEARCH", "Ljava/lang/String;"),
        ],
        "Landroid/server/search/Searchables;": [
            ("F", "buildSearchableList", "()"),
            ("F", "findGlobalSearchActivity", "()"),
        ],
    },
    "CHANGE_WIFI_STATE": {
        "Landroid/net/wifi/IWifiManager$Stub$Proxy;": [
            ("F", "addOrUpdateNetwork", "(Landroid/net/wifi/WifiConfiguration;)"
  ),
            ("F", "disableNetwork", "(I)"),
            ("F", "disconnect", "()"),
            ("F", "enableNetwork", "(I B)"),
            ("F", "pingSupplicant", "()"),
            ("F", "reassociate", "()"),
            ("F", "reconnect", "()"),
            ("F", "removeNetwork", "(I)"),
            ("F", "saveConfiguration", "()"),
            ("F", "setNumAllowedChannels", "(I B)"),
            ("F", "setWifiApEnabled", "(Landroid/net/wifi/WifiConfiguration; B)"
  ),
            ("F", "setWifiEnabled", "(B)"),
            ("F", "startScan", "(B)"),
        ],
        "Landroid/net/wifi/WifiManager;": [
            ("F", "addNetwork", "(Landroid/net/wifi/WifiConfiguration;)"),
            ("F", "addOrUpdateNetwork", "(Landroid/net/wifi/WifiConfiguration;)"
  ),
            ("F", "disableNetwork", "(I)"),
            ("F", "disconnect", "()"),
            ("F", "enableNetwork", "(I B)"),
            ("F", "pingSupplicant", "()"),
            ("F", "reassociate", "()"),
            ("F", "reconnect", "()"),
            ("F", "removeNetwork", "(I)"),
            ("F", "saveConfiguration", "()"),
            ("F", "setNumAllowedChannels", "(I B)"),
            ("F", "setWifiApEnabled", "(Landroid/net/wifi/WifiConfiguration; B)"
  ),
            ("F", "setWifiEnabled", "(B)"),
            ("F", "startScan", "()"),
            ("F", "startScanActive", "()"),
        ],
    },
    "BROADCAST_STICKY": {
        "Landroid/app/ExpandableListActivity;": [
            ("F", "removeStickyBroadcast", "(Landroid/content/Intent;)"),
            ("F", "sendStickyBroadcast", "(Landroid/content/Intent;)"),
            ("F", "sendStickyOrderedBroadcast",
             "(Landroid/content/Intent; Landroid/content/BroadcastReceiver; Landroid/os/Handler; I Ljava/lang/String; Landroid/os/Bundle;)"
  ),
        ],
        "Landroid/accessibilityservice/AccessibilityService;": [
            ("F", "removeStickyBroadcast", "(Landroid/content/Intent;)"),
            ("F", "sendStickyBroadcast", "(Landroid/content/Intent;)"),
            ("F", "sendStickyOrderedBroadcast",
             "(Landroid/content/Intent; Landroid/content/BroadcastReceiver; Landroid/os/Handler; I Ljava/lang/String; Landroid/os/Bundle;)"
  ),
        ],
        "Landroid/accounts/GrantCredentialsPermissionActivity;": [
            ("F", "removeStickyBroadcast", "(Landroid/content/Intent;)"),
            ("F", "sendStickyBroadcast", "(Landroid/content/Intent;)"),
            ("F", "sendStickyOrderedBroadcast",
             "(Landroid/content/Intent; Landroid/content/BroadcastReceiver; Landroid/os/Handler; I Ljava/lang/String; Landroid/os/Bundle;)"
  ),
        ],
        "Landroid/app/backup/BackupAgent;": [
            ("F", "removeStickyBroadcast", "(Landroid/content/Intent;)"),
            ("F", "sendStickyBroadcast", "(Landroid/content/Intent;)"),
            ("F", "sendStickyOrderedBroadcast",
             "(Landroid/content/Intent; Landroid/content/BroadcastReceiver; Landroid/os/Handler; I Ljava/lang/String; Landroid/os/Bundle;)"
  ),
        ],
        "Landroid/service/wallpaper/WallpaperService;": [
            ("F", "removeStickyBroadcast", "(Landroid/content/Intent;)"),
            ("F", "sendStickyBroadcast", "(Landroid/content/Intent;)"),
            ("F", "sendStickyOrderedBroadcast",
             "(Landroid/content/Intent; Landroid/content/BroadcastReceiver; Landroid/os/Handler; I Ljava/lang/String; Landroid/os/Bundle;)"
  ),
        ],
        "Landroid/app/backup/BackupAgentHelper;": [
            ("F", "removeStickyBroadcast", "(Landroid/content/Intent;)"),
            ("F", "sendStickyBroadcast", "(Landroid/content/Intent;)"),
            ("F", "sendStickyOrderedBroadcast",
             "(Landroid/content/Intent; Landroid/content/BroadcastReceiver; Landroid/os/Handler; I Ljava/lang/String; Landroid/os/Bundle;)"
  ),
        ],
        "Landroid/accounts/AccountAuthenticatorActivity;": [
            ("F", "removeStickyBroadcast", "(Landroid/content/Intent;)"),
            ("F", "sendStickyBroadcast", "(Landroid/content/Intent;)"),
            ("F", "sendStickyOrderedBroadcast",
             "(Landroid/content/Intent; Landroid/content/BroadcastReceiver; Landroid/os/Handler; I Ljava/lang/String; Landroid/os/Bundle;)"
  ),
        ],
        "Landroid/app/IActivityManager$Stub$Proxy;": [
            ("F", "unbroadcastIntent",
             "(Landroid/app/IApplicationThread; Landroid/content/Intent;)"),
        ],
        "Landroid/app/ActivityGroup;": [
            ("F", "removeStickyBroadcast", "(Landroid/content/Intent;)"),
            ("F", "sendStickyBroadcast", "(Landroid/content/Intent;)"),
            ("F", "sendStickyOrderedBroadcast",
             "(Landroid/content/Intent; Landroid/content/BroadcastReceiver; Landroid/os/Handler; I Ljava/lang/String; Landroid/os/Bundle;)"
  ),
        ],
        "Landroid/content/ContextWrapper;": [
            ("F", "removeStickyBroadcast", "(Landroid/content/Intent;)"),
            ("F", "sendStickyBroadcast", "(Landroid/content/Intent;)"),
            ("F", "removeStickyBroadcast", "(Landroid/content/Intent;)"),
            ("F", "sendStickyBroadcast", "(Landroid/content/Intent;)"),
            ("F", "sendStickyOrderedBroadcast",
             "(Landroid/content/Intent; Landroid/content/BroadcastReceiver; Landroid/os/Handler; I Ljava/lang/String; Landroid/os/Bundle;)"
  ),
        ],
        "Landroid/app/Activity;": [
            ("F", "removeStickyBroadcast", "(Landroid/content/Intent;)"),
            ("F", "sendStickyBroadcast", "(Landroid/content/Intent;)"),
            ("F", "sendStickyOrderedBroadcast",
             "(Landroid/content/Intent; Landroid/content/BroadcastReceiver; Landroid/os/Handler; I Ljava/lang/String; Landroid/os/Bundle;)"
  ),
        ],
        "Landroid/app/ContextImpl;": [
            ("F", "removeStickyBroadcast", "(Landroid/content/Intent;)"),
            ("F", "sendStickyBroadcast", "(Landroid/content/Intent;)"),
            ("F", "sendStickyOrderedBroadcast",
             "(Landroid/content/Intent; Landroid/content/BroadcastReceiver; Landroid/os/Handler; I Ljava/lang/String; Landroid/os/Bundle;)"
  ),
        ],
        "Landroid/app/AliasActivity;": [
            ("F", "removeStickyBroadcast", "(Landroid/content/Intent;)"),
            ("F", "sendStickyBroadcast", "(Landroid/content/Intent;)"),
            ("F", "sendStickyOrderedBroadcast",
             "(Landroid/content/Intent; Landroid/content/BroadcastReceiver; Landroid/os/Handler; I Ljava/lang/String; Landroid/os/Bundle;)"
  ),
        ],
        "Landroid/content/Context;": [
            ("F", "removeStickyBroadcast", "(Landroid/content/Intent;)"),
            ("F", "sendStickyBroadcast", "(Landroid/content/Intent;)"),
            ("F", "removeStickyBroadcast", "(Landroid/content/Intent;)"),
            ("F", "sendStickyBroadcast", "(Landroid/content/Intent;)"),
            ("F", "sendStickyOrderedBroadcast",
             "(Landroid/content/Intent; Landroid/content/BroadcastReceiver; Landroid/os/Handler; I Ljava/lang/String; Landroid/os/Bundle;)"
  ),
        ],
        "Landroid/service/urlrenderer/UrlRendererService;": [
            ("F", "removeStickyBroadcast", "(Landroid/content/Intent;)"),
            ("F", "sendStickyBroadcast", "(Landroid/content/Intent;)"),
            ("F", "sendStickyOrderedBroadcast",
             "(Landroid/content/Intent; Landroid/content/BroadcastReceiver; Landroid/os/Handler; I Ljava/lang/String; Landroid/os/Bundle;)"
  ),
        ],
        "Landroid/app/FullBackupAgent;": [
            ("F", "removeStickyBroadcast", "(Landroid/content/Intent;)"),
            ("F", "sendStickyBroadcast", "(Landroid/content/Intent;)"),
            ("F", "sendStickyOrderedBroadcast",
             "(Landroid/content/Intent; Landroid/content/BroadcastReceiver; Landroid/os/Handler; I Ljava/lang/String; Landroid/os/Bundle;)"
  ),
        ],
        "Landroid/app/TabActivity;": [
            ("F", "removeStickyBroadcast", "(Landroid/content/Intent;)"),
            ("F", "sendStickyBroadcast", "(Landroid/content/Intent;)"),
            ("F", "sendStickyOrderedBroadcast",
             "(Landroid/content/Intent; Landroid/content/BroadcastReceiver; Landroid/os/Handler; I Ljava/lang/String; Landroid/os/Bundle;)"
  ),
        ],
        "Landroid/view/ContextThemeWrapper;": [
            ("F", "removeStickyBroadcast", "(Landroid/content/Intent;)"),
            ("F", "sendStickyBroadcast", "(Landroid/content/Intent;)"),
            ("F", "sendStickyOrderedBroadcast",
             "(Landroid/content/Intent; Landroid/content/BroadcastReceiver; Landroid/os/Handler; I Ljava/lang/String; Landroid/os/Bundle;)"
  ),
        ],
        "Landroid/speech/RecognitionService;": [
            ("F", "removeStickyBroadcast", "(Landroid/content/Intent;)"),
            ("F", "sendStickyBroadcast", "(Landroid/content/Intent;)"),
            ("F", "sendStickyOrderedBroadcast",
             "(Landroid/content/Intent; Landroid/content/BroadcastReceiver; Landroid/os/Handler; I Ljava/lang/String; Landroid/os/Bundle;)"
  ),
        ],
        "Landroid/app/IntentService;": [
            ("F", "removeStickyBroadcast", "(Landroid/content/Intent;)"),
            ("F", "sendStickyBroadcast", "(Landroid/content/Intent;)"),
            ("F", "sendStickyOrderedBroadcast",
             "(Landroid/content/Intent; Landroid/content/BroadcastReceiver; Landroid/os/Handler; I Ljava/lang/String; Landroid/os/Bundle;)"
  ),
        ],
        "Landroid/inputmethodservice/AbstractInputMethodService;": [
            ("F", "removeStickyBroadcast", "(Landroid/content/Intent;)"),
            ("F", "sendStickyBroadcast", "(Landroid/content/Intent;)"),
            ("F", "sendStickyOrderedBroadcast",
             "(Landroid/content/Intent; Landroid/content/BroadcastReceiver; Landroid/os/Handler; I Ljava/lang/String; Landroid/os/Bundle;)"
  ),
        ],
        "Landroid/app/Application;": [
            ("F", "removeStickyBroadcast", "(Landroid/content/Intent;)"),
            ("F", "sendStickyBroadcast", "(Landroid/content/Intent;)"),
            ("F", "sendStickyOrderedBroadcast",
             "(Landroid/content/Intent; Landroid/content/BroadcastReceiver; Landroid/os/Handler; I Ljava/lang/String; Landroid/os/Bundle;)"
  ),
            ("F", "sendStickyOrderedBroadcast",
             "(Landroid/content/Intent; Landroid/content/BroadcastReceiver; Landroid/os/Handler; I Ljava/lang/String; Landroid/os/Bundle;)"
  ),
        ],
        "Landroid/app/ListActivity;": [
            ("F", "removeStickyBroadcast", "(Landroid/content/Intent;)"),
            ("F", "sendStickyBroadcast", "(Landroid/content/Intent;)"),
            ("F", "sendStickyOrderedBroadcast",
             "(Landroid/content/Intent; Landroid/content/BroadcastReceiver; Landroid/os/Handler; I Ljava/lang/String; Landroid/os/Bundle;)"
  ),
        ],
        "Landroid/app/Service;": [
            ("F", "removeStickyBroadcast", "(Landroid/content/Intent;)"),
            ("F", "sendStickyBroadcast", "(Landroid/content/Intent;)"),
            ("F", "sendStickyOrderedBroadcast",
             "(Landroid/content/Intent; Landroid/content/BroadcastReceiver; Landroid/os/Handler; I Ljava/lang/String; Landroid/os/Bundle;)"
  ),
        ],
        "Landroid/content/MutableContextWrapper;": [
            ("F", "removeStickyBroadcast", "(Landroid/content/Intent;)"),
            ("F", "sendStickyBroadcast", "(Landroid/content/Intent;)"),
            ("F", "sendStickyOrderedBroadcast",
             "(Landroid/content/Intent; Landroid/content/BroadcastReceiver; Landroid/os/Handler; I Ljava/lang/String; Landroid/os/Bundle;)"
  ),
        ],
    },
    "FORCE_STOP_PACKAGES": {
        "Landroid/app/IActivityManager$Stub$Proxy;": [
            ("F", "forceStopPackage", "(Ljava/lang/String;)"),
        ],
        "Landroid/app/ActivityManagerNative;": [
            ("F", "forceStopPackage", "(Ljava/lang/String;)"),
        ],
        "Landroid/app/ActivityManager;": [
            ("F", "forceStopPackage", "(Ljava/lang/String;)"),
        ],
    },
    "KILL_BACKGROUND_PROCESSES": {
        "Landroid/app/IActivityManager$Stub$Proxy;": [
            ("F", "killBackgroundProcesses", "(Ljava/lang/String;)"),
        ],
        "Landroid/app/ActivityManager;": [
            ("F", "killBackgroundProcesses", "(Ljava/lang/String;)"),
        ],
    },
    "SET_TIME_ZONE": {
        "Landroid/app/AlarmManager;": [
            ("F", "setTimeZone", "(Ljava/lang/String;)"),
            ("F", "setTimeZone", "(Ljava/lang/String;)"),
        ],
        "Landroid/app/IAlarmManager$Stub$Proxy;": [
            ("F", "setTimeZone", "(Ljava/lang/String;)"),
        ],
    },
    "BLUETOOTH_ADMIN": {
        "Landroid/server/BluetoothA2dpService;": [
            ("F", "connectSink", "(Landroid/bluetooth/BluetoothDevice;)"),
            ("F", "disconnectSink", "(Landroid/bluetooth/BluetoothDevice;)"),
            ("F", "resumeSink", "(Landroid/bluetooth/BluetoothDevice;)"),
            ("F", "setSinkPriority", "(Landroid/bluetooth/BluetoothDevice; I)"),
            ("F", "setSinkPriority", "(Landroid/bluetooth/BluetoothDevice; I)"),
            ("F", "suspendSink", "(Landroid/bluetooth/BluetoothDevice;)"),
        ],
        "Landroid/bluetooth/BluetoothPbap;": [
            ("F", "disconnect", "()"),
        ],
        "Landroid/bluetooth/IBluetoothA2dp$Stub$Proxy;": [
            ("F", "connectSink", "(Landroid/bluetooth/BluetoothDevice;)"),
            ("F", "disconnectSink", "(Landroid/bluetooth/BluetoothDevice;)"),
            ("F", "resumeSink", "(Landroid/bluetooth/BluetoothDevice;)"),
            ("F", "setSinkPriority", "(Landroid/bluetooth/BluetoothDevice; I)"),
            ("F", "suspendSink", "(Landroid/bluetooth/BluetoothDevice;)"),
        ],
        "Landroid/bluetooth/BluetoothAdapter;": [
            ("F", "cancelDiscovery", "()"),
            ("F", "disable", "()"),
            ("F", "enable", "()"),
            ("F", "setName", "(Ljava/lang/String;)"),
            ("F", "startDiscovery", "()"),
            ("F", "cancelDiscovery", "()"),
            ("F", "disable", "()"),
            ("F", "enable", "()"),
            ("F", "setDiscoverableTimeout", "(I)"),
            ("F", "setName", "(Ljava/lang/String;)"),
            ("F", "startDiscovery", "()"),
        ],
        "Landroid/server/BluetoothService;": [
            ("F", "cancelBondProcess", "(Ljava/lang/String;)"),
            ("F", "cancelDiscovery", "()"),
            ("F", "cancelPairingUserInput", "(Ljava/lang/String;)"),
            ("F", "createBond", "(Ljava/lang/String;)"),
            ("F", "disable", "()"),
            ("F", "disable", "(B)"),
            ("F", "enable", "()"),
            ("F", "enable", "(B)"),
            ("F", "removeBond", "(Ljava/lang/String;)"),
            ("F", "setDiscoverableTimeout", "(I)"),
            ("F", "setName", "(Ljava/lang/String;)"),
            ("F", "setPairingConfirmation", "(Ljava/lang/String; B)"),
            ("F", "setPasskey", "(Ljava/lang/String; I)"),
            ("F", "setPin", "(Ljava/lang/String; [L;)"),
            ("F", "setTrust", "(Ljava/lang/String; B)"),
            ("F", "startDiscovery", "()"),
        ],
        "Landroid/bluetooth/BluetoothHeadset;": [
            ("F", "connectHeadset", "(Landroid/bluetooth/BluetoothDevice;)"),
            ("F", "disconnectHeadset", "()"),
            ("F", "setPriority", "(Landroid/bluetooth/BluetoothDevice; I)"),
        ],
        "Landroid/bluetooth/IBluetoothHeadset$Stub$Proxy;": [
            ("F", "connectHeadset", "(Landroid/bluetooth/BluetoothDevice;)"),
            ("F", "disconnectHeadset", "()"),
            ("F", "setPriority", "(Landroid/bluetooth/BluetoothDevice; I)"),
        ],
        "Landroid/bluetooth/BluetoothDevice;": [
            ("F", "cancelBondProcess", "()"),
            ("F", "cancelPairingUserInput", "()"),
            ("F", "createBond", "()"),
            ("F", "removeBond", "()"),
            ("F", "setPairingConfirmation", "(B)"),
            ("F", "setPasskey", "(I)"),
            ("F", "setPin", "([L;)"),
        ],
        "Landroid/bluetooth/IBluetoothPbap$Stub$Proxy;": [
            ("F", "connect", "(Landroid/bluetooth/BluetoothDevice;)"),
            ("F", "disconnect", "()"),
        ],
        "Landroid/bluetooth/BluetoothA2dp;": [
            ("F", "connectSink", "(Landroid/bluetooth/BluetoothDevice;)"),
            ("F", "disconnectSink", "(Landroid/bluetooth/BluetoothDevice;)"),
            ("F", "resumeSink", "(Landroid/bluetooth/BluetoothDevice;)"),
            ("F", "setSinkPriority", "(Landroid/bluetooth/BluetoothDevice; I)"),
            ("F", "suspendSink", "(Landroid/bluetooth/BluetoothDevice;)"),
        ],
        "Landroid/bluetooth/IBluetooth$Stub$Proxy;": [
            ("F", "cancelBondProcess", "(Ljava/lang/String;)"),
            ("F", "cancelDiscovery", "()"),
            ("F", "cancelPairingUserInput", "(Ljava/lang/String;)"),
            ("F", "createBond", "(Ljava/lang/String;)"),
            ("F", "disable", "(B)"),
            ("F", "enable", "()"),
            ("F", "removeBond", "(Ljava/lang/String;)"),
            ("F", "setDiscoverableTimeout", "(I)"),
            ("F", "setName", "(Ljava/lang/String;)"),
            ("F", "setPairingConfirmation", "(Ljava/lang/String; B)"),
            ("F", "setPasskey", "(Ljava/lang/String; I)"),
            ("F", "setPin", "(Ljava/lang/String; [L;)"),
            ("F", "setTrust", "(Ljava/lang/String; B)"),
            ("F", "startDiscovery", "()"),
        ],
    },
    "INJECT_EVENTS": {
        "Landroid/view/IWindowManager$Stub$Proxy;": [
            ("F", "injectKeyEvent", "(Landroid/view/KeyEvent; B)"),
            ("F", "injectPointerEvent", "(Landroid/view/MotionEvent; B)"),
            ("F", "injectTrackballEvent", "(Landroid/view/MotionEvent; B)"),
        ],
        "Landroid/app/Instrumentation;": [
            ("F", "invokeContextMenuAction", "(Landroid/app/Activity; I I)"),
            ("F", "sendCharacterSync", "(I)"),
            ("F", "sendKeyDownUpSync", "(I)"),
            ("F", "sendKeySync", "(Landroid/view/KeyEvent;)"),
            ("F", "sendPointerSync", "(Landroid/view/MotionEvent;)"),
            ("F", "sendStringSync", "(Ljava/lang/String;)"),
            ("F", "sendTrackballEventSync", "(Landroid/view/MotionEvent;)"),
        ],
    },
    "CAMERA": {
        "Landroid/hardware/Camera/ErrorCallback;": [
            ("F", "onError", "(I Landroid/hardware/Camera;)"),
        ],
        "Landroid/media/MediaRecorder;": [
            ("F", "setVideoSource", "(I)"),
        ],
        "Landroid/view/KeyEvent;": [
            ("C", "KEYCODE_CAMERA", "I"),
        ],
        "Landroid/bluetooth/BluetoothClass/Device;": [
            ("C", "AUDIO_VIDEO_VIDEO_CAMERA", "I"),
        ],
        "Landroid/provider/MediaStore;": [
            ("C", "INTENT_ACTION_STILL_IMAGE_CAMERA", "Ljava/lang/String;"),
            ("C", "INTENT_ACTION_VIDEO_CAMERA", "Ljava/lang/String;"),
        ],
        "Landroid/hardware/Camera/CameraInfo;": [
            ("C", "CAMERA_FACING_BACK", "I"),
            ("C", "CAMERA_FACING_FRONT", "I"),
            ("C", "facing", "I"),
        ],
        "Landroid/provider/ContactsContract/StatusColumns;": [
            ("C", "CAPABILITY_HAS_CAMERA", "I"),
        ],
        "Landroid/hardware/Camera/Parameters;": [
            ("F", "setRotation", "(I)"),
        ],
        "Landroid/media/MediaRecorder/VideoSource;": [
            ("C", "CAMERA", "I"),
        ],
        "Landroid/content/Intent;": [
            ("C", "IntentResolution", "Ljava/lang/String;"),
            ("C", "ACTION_CAMERA_BUTTON", "Ljava/lang/String;"),
        ],
        "Landroid/content/pm/PackageManager;": [
            ("C", "FEATURE_CAMERA", "Ljava/lang/String;"),
            ("C", "FEATURE_CAMERA_AUTOFOCUS", "Ljava/lang/String;"),
            ("C", "FEATURE_CAMERA_FLASH", "Ljava/lang/String;"),
            ("C", "FEATURE_CAMERA_FRONT", "Ljava/lang/String;"),
        ],
        "Landroid/hardware/Camera;": [
            ("C", "CAMERA_ERROR_SERVER_DIED", "I"),
            ("C", "CAMERA_ERROR_UNKNOWN", "I"),
            ("F", "setDisplayOrientation", "(I)"),
            ("F", "native_setup", "(Ljava/lang/Object;)"),
            ("F", "open", "()"),
        ],
    },
    "SET_WALLPAPER": {
        "Landroid/app/Activity;": [
            ("F", "clearWallpaper", "()"),
            ("F", "setWallpaper", "(Landroid/graphics/Bitmap;)"),
            ("F", "setWallpaper", "(Ljava/io/InputStream;)"),
        ],
        "Landroid/app/ExpandableListActivity;": [
            ("F", "clearWallpaper", "()"),
            ("F", "setWallpaper", "(Landroid/graphics/Bitmap;)"),
            ("F", "setWallpaper", "(Ljava/io/InputStream;)"),
        ],
        "Landroid/accessibilityservice/AccessibilityService;": [
            ("F", "clearWallpaper", "()"),
            ("F", "setWallpaper", "(Landroid/graphics/Bitmap;)"),
            ("F", "setWallpaper", "(Ljava/io/InputStream;)"),
        ],
        "Landroid/accounts/GrantCredentialsPermissionActivity;": [
            ("F", "clearWallpaper", "()"),
            ("F", "setWallpaper", "(Landroid/graphics/Bitmap;)"),
            ("F", "setWallpaper", "(Ljava/io/InputStream;)"),
        ],
        "Landroid/app/backup/BackupAgent;": [
            ("F", "clearWallpaper", "()"),
            ("F", "setWallpaper", "(Landroid/graphics/Bitmap;)"),
            ("F", "setWallpaper", "(Ljava/io/InputStream;)"),
        ],
        "Landroid/service/wallpaper/WallpaperService;": [
            ("F", "clearWallpaper", "()"),
            ("F", "setWallpaper", "(Landroid/graphics/Bitmap;)"),
            ("F", "setWallpaper", "(Ljava/io/InputStream;)"),
        ],
        "Landroid/app/backup/BackupAgentHelper;": [
            ("F", "clearWallpaper", "()"),
            ("F", "setWallpaper", "(Landroid/graphics/Bitmap;)"),
            ("F", "setWallpaper", "(Ljava/io/InputStream;)"),
        ],
        "Landroid/accounts/AccountAuthenticatorActivity;": [
            ("F", "clearWallpaper", "()"),
            ("F", "setWallpaper", "(Landroid/graphics/Bitmap;)"),
            ("F", "setWallpaper", "(Ljava/io/InputStream;)"),
        ],
        "Landroid/app/IWallpaperManager$Stub$Proxy;": [
            ("F", "setWallpaper", "(Ljava/lang/String;)"),
        ],
        "Landroid/app/ActivityGroup;": [
            ("F", "clearWallpaper", "()"),
            ("F", "setWallpaper", "(Landroid/graphics/Bitmap;)"),
            ("F", "setWallpaper", "(Ljava/io/InputStream;)"),
        ],
        "Landroid/content/ContextWrapper;": [
            ("F", "clearWallpaper", "()"),
            ("F", "setWallpaper", "(Landroid/graphics/Bitmap;)"),
            ("F", "setWallpaper", "(Ljava/io/InputStream;)"),
        ],
        "Landroid/app/WallpaperManager;": [
            ("F", "setBitmap", "(Landroid/graphics/Bitmap;)"),
            ("F", "clear", "()"),
            ("F", "setBitmap", "(Landroid/graphics/Bitmap;)"),
            ("F", "setResource", "(I)"),
            ("F", "setStream", "(Ljava/io/InputStream;)"),
        ],
        "Landroid/app/ContextImpl;": [
            ("F", "clearWallpaper", "()"),
            ("F", "setWallpaper", "(Landroid/graphics/Bitmap;)"),
            ("F", "setWallpaper", "(Ljava/io/InputStream;)"),
        ],
        "Landroid/app/AliasActivity;": [
            ("F", "clearWallpaper", "()"),
            ("F", "setWallpaper", "(Landroid/graphics/Bitmap;)"),
            ("F", "setWallpaper", "(Ljava/io/InputStream;)"),
        ],
        "Landroid/content/Context;": [
            ("F", "clearWallpaper", "()"),
            ("F", "setWallpaper", "(Landroid/graphics/Bitmap;)"),
            ("F", "setWallpaper", "(Ljava/io/InputStream;)"),
        ],
        "Landroid/service/urlrenderer/UrlRendererService;": [
            ("F", "clearWallpaper", "()"),
            ("F", "setWallpaper", "(Landroid/graphics/Bitmap;)"),
            ("F", "setWallpaper", "(Ljava/io/InputStream;)"),
        ],
        "Landroid/app/FullBackupAgent;": [
            ("F", "clearWallpaper", "()"),
            ("F", "setWallpaper", "(Landroid/graphics/Bitmap;)"),
            ("F", "setWallpaper", "(Ljava/io/InputStream;)"),
        ],
        "Landroid/app/TabActivity;": [
            ("F", "clearWallpaper", "()"),
            ("F", "setWallpaper", "(Landroid/graphics/Bitmap;)"),
            ("F", "setWallpaper", "(Ljava/io/InputStream;)"),
        ],
        "Landroid/view/ContextThemeWrapper;": [
            ("F", "clearWallpaper", "()"),
            ("F", "setWallpaper", "(Landroid/graphics/Bitmap;)"),
            ("F", "setWallpaper", "(Ljava/io/InputStream;)"),
        ],
        "Landroid/speech/RecognitionService;": [
            ("F", "clearWallpaper", "()"),
            ("F", "setWallpaper", "(Landroid/graphics/Bitmap;)"),
            ("F", "setWallpaper", "(Ljava/io/InputStream;)"),
        ],
        "Landroid/app/IntentService;": [
            ("F", "clearWallpaper", "()"),
            ("F", "setWallpaper", "(Landroid/graphics/Bitmap;)"),
            ("F", "setWallpaper", "(Ljava/io/InputStream;)"),
        ],
        "Landroid/inputmethodservice/AbstractInputMethodService;": [
            ("F", "clearWallpaper", "()"),
            ("F", "setWallpaper", "(Landroid/graphics/Bitmap;)"),
            ("F", "setWallpaper", "(Ljava/io/InputStream;)"),
        ],
        "Landroid/app/Application;": [
            ("F", "clearWallpaper", "()"),
            ("F", "setWallpaper", "(Landroid/graphics/Bitmap;)"),
            ("F", "setWallpaper", "(Ljava/io/InputStream;)"),
        ],
        "Landroid/app/ListActivity;": [
            ("F", "clearWallpaper", "()"),
            ("F", "setWallpaper", "(Landroid/graphics/Bitmap;)"),
            ("F", "setWallpaper", "(Ljava/io/InputStream;)"),
        ],
        "Landroid/app/Service;": [
            ("F", "clearWallpaper", "()"),
            ("F", "setWallpaper", "(Landroid/graphics/Bitmap;)"),
            ("F", "setWallpaper", "(Ljava/io/InputStream;)"),
        ],
        "Landroid/content/MutableContextWrapper;": [
            ("F", "clearWallpaper", "()"),
            ("F", "setWallpaper", "(Landroid/graphics/Bitmap;)"),
            ("F", "setWallpaper", "(Ljava/io/InputStream;)"),
        ],
    },
    "WAKE_LOCK": {
        "Landroid/net/wifi/IWifiManager$Stub$Proxy;": [
            ("F", "acquireWifiLock",
             "(Landroid/os/IBinder; I Ljava/lang/String;)"),
            ("F", "releaseWifiLock", "(Landroid/os/IBinder;)"),
        ],
        "Landroid/bluetooth/HeadsetBase;": [
            ("F", "acquireWakeLock", "()"),
            ("F", "finalize", "()"),
            ("F", "handleInput", "(Ljava/lang/String;)"),
            ("F", "releaseWakeLock", "()"),
        ],
        "Landroid/os/PowerManager$WakeLock;": [
            ("F", "acquire", "()"),
            ("F", "acquire", "(J)"),
            ("F", "release", "()"),
            ("F", "release", "(I)"),
        ],
        "Landroid/media/MediaPlayer;": [
            ("F", "setWakeMode", "(Landroid/content/Context; I)"),
            ("F", "start", "()"),
            ("F", "stayAwake", "(B)"),
            ("F", "stop", "()"),
        ],
        "Landroid/bluetooth/ScoSocket;": [
            ("F", "acquireWakeLock", "()"),
            ("F", "close", "()"),
            ("F", "finalize", "()"),
            ("F", "releaseWakeLock", "()"),
            ("F", "releaseWakeLockNow", "()"),
        ],
        "Landroid/media/AsyncPlayer;": [
            ("F", "acquireWakeLock", "()"),
            ("F", "enqueueLocked", "(Landroid/media/AsyncPlayer$Command;)"),
            ("F", "play", "(Landroid/content/Context; Landroid/net/Uri; B I)"),
            ("F", "releaseWakeLock", "()"),
            ("F", "stop", "()"),
        ],
        "Landroid/net/wifi/WifiManager$WifiLock;": [
            ("F", "acquire", "()"),
            ("F", "finalize", "()"),
            ("F", "release", "()"),
        ],
        "Landroid/os/IPowerManager$Stub$Proxy;": [
            ("F", "acquireWakeLock",
             "(I Landroid/os/IBinder; Ljava/lang/String;)"),
            ("F", "releaseWakeLock", "(Landroid/os/IBinder; I)"),
        ],
        "Landroid/net/sip/SipAudioCall;": [
            ("F", "startAudio", "()"),
        ],
        "Landroid/os/PowerManager;": [
            ("C", "ACQUIRE_CAUSES_WAKEUP", "I"),
            ("C", "FULL_WAKE_LOCK", "I"),
            ("C", "ON_AFTER_RELEASE", "I"),
            ("C", "PARTIAL_WAKE_LOCK", "I"),
            ("C", "SCREEN_BRIGHT_WAKE_LOCK", "I"),
            ("C", "SCREEN_DIM_WAKE_LOCK", "I"),
            ("F", "newWakeLock", "(I Ljava/lang/String;)"),
        ],
    },
    "MANAGE_ACCOUNTS": {
        "Landroid/accounts/AccountManager;": [
            ("F", "addAccount",
             "(Ljava/lang/String; Ljava/lang/String; [Ljava/lang/String; Landroid/os/Bundle; Landroid/app/Activity; Landroid/accounts/AccountManagerCallback<android/os/Bundle>; Landroid/os/Handler;)"
  ),
            ("F", "clearPassword", "(Landroid/accounts/Account;)"),
            ("F", "confirmCredentials",
             "(Landroid/accounts/Account; Landroid/os/Bundle; Landroid/app/Activity; Landroid/accounts/AccountManagerCallback<android/os/Bundle>; Landroid/os/Handler;)"
  ),
            ("F", "editProperties",
             "(Ljava/lang/String; Landroid/app/Activity; Landroid/accounts/AccountManagerCallback<android/os/Bundle>; Landroid/os/Handler;)"
  ),
            ("F", "getAuthTokenByFeatures",
             "(Ljava/lang/String; Ljava/lang/String; [Ljava/lang/String; Landroid/app/Activity; Landroid/os/Bundle; Landroid/os/Bundle; Landroid/accounts/AccountManagerCallback<android/os/Bundle>; Landroid/os/Handler;)"
  ),
            ("F", "invalidateAuthToken",
             "(Ljava/lang/String; Ljava/lang/String;)"),
            ("F", "removeAccount",
             "(Landroid/accounts/Account; Landroid/accounts/AccountManagerCallback<java/lang/Boolean>; Landroid/os/Handler;)"
  ),
            ("F", "updateCredentials",
             "(Landroid/accounts/Account; Ljava/lang/String; Landroid/os/Bundle; Landroid/app/Activity; Landroid/accounts/AccountManagerCallback<android/os/Bundle>; Landroid/os/Handler;)"
  ),
            ("F", "addAccount",
             "(Ljava/lang/String; Ljava/lang/String; [L[Ljava/lang/Strin; Landroid/os/Bundle; Landroid/app/Activity; Landroid/accounts/AccountManagerCallback; Landroid/os/Handler;)"
  ),
            ("F", "clearPassword", "(Landroid/accounts/Account;)"),
            ("F", "confirmCredentials",
             "(Landroid/accounts/Account; Landroid/os/Bundle; Landroid/app/Activity; Landroid/accounts/AccountManagerCallback; Landroid/os/Handler;)"
  ),
            ("F", "editProperties",
             "(Ljava/lang/String; Landroid/app/Activity; Landroid/accounts/AccountManagerCallback; Landroid/os/Handler;)"
  ),
            ("F", "invalidateAuthToken",
             "(Ljava/lang/String; Ljava/lang/String;)"),
            ("F", "removeAccount",
             "(Landroid/accounts/Account; Landroid/accounts/AccountManagerCallback; Landroid/os/Handler;)"
  ),
            ("F", "updateCredentials",
             "(Landroid/accounts/Account; Ljava/lang/String; Landroid/os/Bundle; Landroid/app/Activity; Landroid/accounts/AccountManagerCallback; Landroid/os/Handler;)"
  ),
        ],
        "Landroid/accounts/AccountManagerService;": [
            ("F", "addAcount",
             "(Landroid/accounts/IAccountManagerResponse; Ljava/lang/String; Ljava/lang/String; [L[Ljava/lang/Strin; B Landroid/os/Bundle;)"
  ),
            ("F", "checkManageAccountsOrUseCredentialsPermissions", "()"),
            ("F", "checkManageAccountsPermission", "()"),
            ("F", "clearPassword", "(Landroid/accounts/Account;)"),
            ("F", "confirmCredentials",
             "(Landroid/accounts/IAccountManagerResponse; Landroid/accounts/Account; Landroid/os/Bundle; B)"
  ),
            ("F", "editProperties",
             "(Landroid/accounts/IAccountManagerResponse; Ljava/lang/String; B)"
  ),
            ("F", "invalidateAuthToken",
             "(Ljava/lang/String; Ljava/lang/String;)"),
            ("F", "removeAccount",
             "(Landroid/accounts/IAccountManagerResponse; Landroid/accounts/Account;)"
  ),
            ("F", "updateCredentials",
             "(Landroid/accounts/IAccountManagerResponse; Landroid/accounts/Account; Ljava/lang/String; B Landroid/os/Bundle;)"
  ),
        ],
        "Landroid/accounts/IAccountManager$Stub$Proxy;": [
            ("F", "addAcount",
             "(Landroid/accounts/IAccountManagerResponse; Ljava/lang/String; Ljava/lang/String; [L[Ljava/lang/Strin; B Landroid/os/Bundle;)"
  ),
            ("F", "clearPassword", "(Landroid/accounts/Account;)"),
            ("F", "confirmCredentials",
             "(Landroid/accounts/IAccountManagerResponse; Landroid/accounts/Account; Landroid/os/Bundle; B)"
  ),
            ("F", "editProperties",
             "(Landroid/accounts/IAccountManagerResponse; Ljava/lang/String; B)"
  ),
            ("F", "invalidateAuthToken",
             "(Ljava/lang/String; Ljava/lang/String;)"),
            ("F", "removeAccount",
             "(Landroid/accounts/IAccountManagerResponse; Landroid/accounts/Account;)"
  ),
            ("F", "updateCredentials",
             "(Landroid/accounts/IAccountManagerResponse; Landroid/accounts/Account; Ljava/lang/String; B Landroid/os/Bundle;)"
  ),
        ],
    },
    "WRITE_CALENDAR": {
        "Landroid/provider/Calendar$CalendarAlerts;": [
            ("F", "insert", "(Landroid/content/ContentResolver; J J J J I)"),
        ],
        "Landroid/provider/Calendar$Calendars;": [
            ("F", "delete",
             "(Landroid/content/ContentResolver; Ljava/lang/String; [L[Ljava/lang/Strin;)"
  ),
            ("F", "deleteCalendarsForAccount",
             "(Landroid/content/ContentResolver; Landroid/accounts/Account;)"),
        ],
    },
    "BIND_APPWIDGET": {
        "Landroid/appwidget/AppWidgetManager;": [
            ("F", "bindAppWidgetId", "(I Landroid/content/ComponentName;)"),
        ],
        "Lcom/android/internal/appwidget/IAppWidgetService$Stub$Proxy;": [
            ("F", "bindAppWidgetId", "(I LComponentName;)"),
        ],
    },
    "ASEC_MOUNT_UNMOUNT": {
        "Landroid/os/storage/IMountService$Stub$Proxy;": [
            ("F", "mountSecureContainer",
             "(Ljava/lang/String; Ljava/lang/String; I)"),
            ("F", "unmountSecureContainer", "(Ljava/lang/String; B)"),
        ],
    },
    "SET_PREFERRED_APPLICATIONS": {
        "Landroid/app/ContextImpl$ApplicationPackageManager;": [
            ("F", "addPreferredActivity",
             "(LIntentFilter; I [LComponentName; LComponentName;)"),
            ("F", "clearPackagePreferredActivities", "(Ljava/lang/String;)"),
            ("F", "replacePreferredActivity",
             "(LIntentFilter; I [LComponentName; LComponentName;)"),
            ("F", "addPreferredActivity",
             "(Landroid/content/IntentFilter; I [Landroid/content/ComponentName; Landroid/content/ComponentName;)"
  ),
            ("F", "clearPackagePreferredActivities", "(Ljava/lang/String;)"),
            ("F", "replacePreferredActivity",
             "(Landroid/content/IntentFilter; I [Landroid/content/ComponentName; Landroid/content/ComponentName;)"
  ),
        ],
        "Landroid/content/pm/PackageManager;": [
            ("F", "addPreferredActivity",
             "(Landroid/content/IntentFilter; I [Landroid/content/ComponentName; Landroid/content/ComponentName;)"
  ),
            ("F", "clearPackagePreferredActivities", "(Ljava/lang/String;)"),
            ("F", "replacePreferredActivity",
             "(Landroid/content/IntentFilter; I [Landroid/content/ComponentName; Landroid/content/ComponentName;)"
  ),
        ],
        "Landroid/content/pm/IPackageManager$Stub$Proxy;": [
            ("F", "addPreferredActivity",
             "(Landroid/content/IntentFilter; I [L[Landroid/content/ComponentNam; Landroid/content/ComponentName;)"
  ),
            ("F", "clearPackagePreferredActivities", "(Ljava/lang/String;)"),
            ("F", "replacePreferredActivity",
             "(Landroid/content/IntentFilter; I [L[Landroid/content/ComponentNam; Landroid/content/ComponentName;)"
  ),
        ],
    },
    "NFC": {
        "Landroid/inputmethodservice/InputMethodService;": [
            ("C", "SoftInputView", "I"),
            ("C", "CandidatesView", "I"),
            ("C", "FullscreenMode", "I"),
            ("C", "GeneratingText", "I"),
        ],
        "Landroid/nfc/tech/NfcA;": [
            ("F", "close", "()"),
            ("F", "connect", "()"),
            ("F", "get", "(Landroid/nfc/Tag;)"),
            ("F", "transceive", "([B)"),
        ],
        "Landroid/nfc/tech/NfcB;": [
            ("F", "close", "()"),
            ("F", "connect", "()"),
            ("F", "get", "(Landroid/nfc/Tag;)"),
            ("F", "transceive", "([B)"),
        ],
        "Landroid/nfc/NfcAdapter;": [
            ("C", "ACTION_TECH_DISCOVERED", "Ljava/lang/String;"),
            ("F", "disableForegroundDispatch", "(Landroid/app/Activity;)"),
            ("F", "disableForegroundNdefPush", "(Landroid/app/Activity;)"),
            ("F", "enableForegroundDispatch",
             "(Landroid/app/Activity; Landroid/app/PendingIntent; [Landroid/content/IntentFilter; [[Ljava/lang/Stringcollections.deque();)"
  ),
            ("F", "enableForegroundNdefPush",
             "(Landroid/app/Activity; Landroid/nfc/NdefMessage;)"),
            ("F", "getDefaultAdapter", "()"),
            ("F", "getDefaultAdapter", "(Landroid/content/Context;)"),
            ("F", "isEnabled", "()"),
        ],
        "Landroid/nfc/tech/NfcF;": [
            ("F", "close", "()"),
            ("F", "connect", "()"),
            ("F", "get", "(Landroid/nfc/Tag;)"),
            ("F", "transceive", "([B)"),
        ],
        "Landroid/nfc/tech/NdefFormatable;": [
            ("F", "close", "()"),
            ("F", "connect", "()"),
            ("F", "format", "(Landroid/nfc/NdefMessage;)"),
            ("F", "formatReadOnly", "(Landroid/nfc/NdefMessage;)"),
        ],
        "Landroid/app/Activity;": [
            ("C", "Fragments", "I"),
            ("C", "ActivityLifecycle", "I"),
            ("C", "ConfigurationChanges", "I"),
            ("C", "StartingActivities", "I"),
            ("C", "SavingPersistentState", "I"),
            ("C", "Permissions", "I"),
            ("C", "ProcessLifecycle", "I"),
        ],
        "Landroid/nfc/tech/MifareClassic;": [
            ("C", "KEY_NFC_FORUM", "[B"),
            ("F", "authenticateSectorWithKeyA", "(I [B)"),
            ("F", "authenticateSectorWithKeyB", "(I [B)"),
            ("F", "close", "()"),
            ("F", "connect", "()"),
            ("F", "decrement", "(I I)"),
            ("F", "increment", "(I I)"),
            ("F", "readBlock", "(I)"),
            ("F", "restore", "(I)"),
            ("F", "transceive", "([B)"),
            ("F", "transfer", "(I)"),
            ("F", "writeBlock", "(I [B)"),
        ],
        "Landroid/nfc/Tag;": [
            ("F", "getTechList", "()"),
        ],
        "Landroid/app/Service;": [
            ("C", "WhatIsAService", "I"),
            ("C", "ServiceLifecycle", "I"),
            ("C", "Permissions", "I"),
            ("C", "ProcessLifecycle", "I"),
            ("C", "LocalServiceSample", "I"),
            ("C", "RemoteMessengerServiceSample", "I"),
        ],
        "Landroid/nfc/NfcManager;": [
            ("F", "getDefaultAdapter", "()"),
        ],
        "Landroid/nfc/tech/MifareUltralight;": [
            ("F", "close", "()"),
            ("F", "connect", "()"),
            ("F", "readPages", "(I)"),
            ("F", "transceive", "([B)"),
            ("F", "writePage", "(I [B)"),
        ],
        "Landroid/nfc/tech/NfcV;": [
            ("F", "close", "()"),
            ("F", "connect", "()"),
            ("F", "get", "(Landroid/nfc/Tag;)"),
            ("F", "transceive", "([B)"),
        ],
        "Landroid/nfc/tech/TagTechnology;": [
            ("F", "close", "()"),
            ("F", "connect", "()"),
        ],
        "Landroid/preference/PreferenceActivity;": [
            ("C", "SampleCode", "Ljava/lang/String;"),
        ],
        "Landroid/content/pm/PackageManager;": [
            ("C", "FEATURE_NFC", "Ljava/lang/String;"),
        ],
        "Landroid/content/Context;": [
            ("C", "NFC_SERVICE", "Ljava/lang/String;"),
        ],
        "Landroid/nfc/tech/Ndef;": [
            ("C", "NFC_FORUM_TYPE_1", "Ljava/lang/String;"),
            ("C", "NFC_FORUM_TYPE_2", "Ljava/lang/String;"),
            ("C", "NFC_FORUM_TYPE_3", "Ljava/lang/String;"),
            ("C", "NFC_FORUM_TYPE_4", "Ljava/lang/String;"),
            ("F", "close", "()"),
            ("F", "connect", "()"),
            ("F", "getType", "()"),
            ("F", "isWritable", "()"),
            ("F", "makeReadOnly", "()"),
            ("F", "writeNdefMessage", "(Landroid/nfc/NdefMessage;)"),
        ],
        "Landroid/nfc/tech/IsoDep;": [
            ("F", "close", "()"),
            ("F", "connect", "()"),
            ("F", "setTimeout", "(I)"),
            ("F", "transceive", "([B)"),
        ],
    },
    "CALL_PHONE": {
        "Lcom/android/internal/telephony/ITelephony$Stub$Proxy;": [
            ("F", "call", "(Ljava/lang/String;)"),
            ("F", "endCall", "()"),
        ],
    },
    "INTERNET": {
        "Lcom/android/http/multipart/FilePart;": [
            ("F", "sendData", "(Ljava/io/OutputStream;)"),
            ("F", "sendDispositionHeader", "(Ljava/io/OutputStream;)"),
        ],
        "Ljava/net/HttpURLConnection;": [
            ("F", "<init>", "(Ljava/net/URL;)"),
            ("F", "connect", "()"),
        ],
        "Landroid/webkit/WebSettings;": [
            ("F", "setBlockNetworkLoads", "(B)"),
            ("F", "verifyNetworkAccess", "()"),
        ],
        "Lorg/apache/http/impl/client/DefaultHttpClient;": [
            ("F", "<init>", "()"),
            ("F", "<init>", "(Lorg/apache/http/params/HttpParams;)"),
            ("F", "<init>",
             "(Lorg/apache/http/conn/ClientConnectionManager; Lorg/apache/http/params/HttpParams;)"
  ),
            ("F", "execute", "(Lorg/apache/http/client/methods/HttpUriRequest;)"
  ),
            ("F", "execute",
             "(Lorg/apache/http/client/methods/HttpUriRequest; Lorg/apache/http/client/ResponseHandler; Lorg/apache/http/protocol/HttpContext;)"
  ),
            ("F", "execute",
             "(Lorg/apache/http/HttpHost; Lorg/apache/http/client/methods/HttpUriRequest; Lorg/apache/http/client/ResponseHandler; Lorg/apache/http/protocol/HttpContext;)"
  ),
            ("F", "execute",
             "(Lorg/apache/http/client/methods/HttpUriRequest; Lorg/apache/http/protocol/HttpContext;)"
  ),
            ("F", "execute",
             "(Lorg/apache/http/client/methods/HttpUriRequest; Lorg/apache/http/client/ResponseHandler;)"
  ),
            ("F", "execute",
             "(Lorg/apache/http/HttpHost; Lorg/apache/http/client/methods/HttpUriRequest; Lorg/apache/http/client/ResponseHandler;)"
  ),
            ("F", "execute",
             "(Lorg/apache/http/HttpHost; Lorg/apache/http/client/methods/HttpUriRequest;)"
  ),
            ("F", "execute",
             "(Lorg/apache/http/HttpHost; Lorg/apache/http/client/methods/HttpUriRequest; Lorg/apache/http/protocol/HttpContext;)"
  ),
        ],
        "Lorg/apache/http/impl/client/HttpClient;": [
            ("F", "execute", "(Lorg/apache/http/client/methods/HttpUriRequest;)"
  ),
            ("F", "execute",
             "(Lorg/apache/http/client/methods/HttpUriRequest; Lorg/apache/http/client/ResponseHandler; Lorg/apache/http/protocol/HttpContext;)"
  ),
            ("F", "execute",
             "(Lorg/apache/http/HttpHost; Lorg/apache/http/client/methods/HttpUriRequest; Lorg/apache/http/client/ResponseHandler; Lorg/apache/http/protocol/HttpContext;)"
  ),
            ("F", "execute",
             "(Lorg/apache/http/client/methods/HttpUriRequest; Lorg/apache/http/protocol/HttpContext;)"
  ),
            ("F", "execute",
             "(Lorg/apache/http/client/methods/HttpUriRequest; Lorg/apache/http/client/ResponseHandler;)"
  ),
            ("F", "execute",
             "(Lorg/apache/http/HttpHost; Lorg/apache/http/client/methods/HttpUriRequest; Lorg/apache/http/client/ResponseHandler;)"
  ),
            ("F", "execute",
             "(Lorg/apache/http/HttpHost; Lorg/apache/http/client/methods/HttpUriRequest;)"
  ),
            ("F", "execute",
             "(Lorg/apache/http/HttpHost; Lorg/apache/http/client/methods/HttpUriRequest; Lorg/apache/http/protocol/HttpContext;)"
  ),
        ],
        "Lcom/android/http/multipart/Part;": [
            ("F", "send", "(Ljava/io/OutputStream;)"),
            ("F", "sendParts",
             "(Ljava/io/OutputStream; [Lcom/android/http/multipart/Part;)"),
            ("F", "sendParts",
             "(Ljava/io/OutputStream; [Lcom/android/http/multipart/Part; [B)"),
            ("F", "sendStart", "(Ljava/io/OutputStream;)"),
            ("F", "sendTransferEncodingHeader", "(Ljava/io/OutputStream;)"),
        ],
        "Landroid/drm/DrmErrorEvent;": [
            ("C", "TYPE_NO_INTERNET_CONNECTION", "I"),
        ],
        "Landroid/webkit/WebViewCore;": [
            ("F", "<init>",
             "(Landroid/content/Context; Landroid/webkit/WebView; Landroid/webkit/CallbackProxy; Ljava/util/Map;)"
  ),
        ],
        "Ljava/net/URLConnection;": [
            ("F", "connect", "()"),
            ("F", "getInputStream", "()"),
        ],
        "Landroid/app/Activity;": [
            ("F", "setContentView", "(I)"),
        ],
        "Ljava/net/MulticastSocket;": [
            ("F", "<init>", "()"),
            ("F", "<init>", "(I)"),
            ("F", "<init>", "(Ljava/net/SocketAddress;)"),
        ],
        "Lcom/android/http/multipart/StringPart;": [
            ("F", "sendData", "(Ljava/io/OuputStream;)"),
        ],
        "Ljava/net/URL;": [
            ("F", "getContent", "([Ljava/lang/Class;)"),
            ("F", "getContent", "()"),
            ("F", "openConnection", "(Ljava/net/Proxy;)"),
            ("F", "openConnection", "()"),
            ("F", "openStream", "()"),
        ],
        "Ljava/net/DatagramSocket;": [
            ("F", "<init>", "()"),
            ("F", "<init>", "(I)"),
            ("F", "<init>", "(I Ljava/net/InetAddress;)"),
            ("F", "<init>", "(Ljava/net/SocketAddress;)"),
        ],
        "Ljava/net/ServerSocket;": [
            ("F", "<init>", "()"),
            ("F", "<init>", "(I)"),
            ("F", "<init>", "(I I)"),
            ("F", "<init>", "(I I Ljava/net/InetAddress;)"),
            ("F", "bind", "(Ljava/net/SocketAddress;)"),
            ("F", "bind", "(Ljava/net/SocketAddress; I)"),
        ],
        "Ljava/net/Socket;": [
            ("F", "<init>", "()"),
            ("F", "<init>", "(Ljava/lang/String; I)"),
            ("F", "<init>", "(Ljava/lang/String; I Ljava/net/InetAddress; I)"),
            ("F", "<init>", "(Ljava/lang/String; I B)"),
            ("F", "<init>", "(Ljava/net/InetAddress; I)"),
            ("F", "<init>",
             "(Ljava/net/InetAddress; I Ljava/net/InetAddress; I)"),
            ("F", "<init>", "(Ljava/net/InetAddress; I B)"),
        ],
        "Landroid/webkit/WebView;": [
            ("F", "<init>",
             "(Landroid/content/Context; Landroid/util/AttributeSet; I)"),
            ("F", "<init>",
             "(Landroid/content/Context; Landroid/util/AttributeSet;)"),
            ("F", "<init>", "(Landroid/content/Context;)"),
        ],
        "Ljava/net/NetworkInterface;": [
            ("F", "<init>", "()"),
            ("F", "<init>", "(Ljava/lang/String; I Ljava/net/InetAddress;)"),
        ],
    },
    "ACCESS_FINE_LOCATION": {
        "Landroid/webkit/WebChromeClient;": [
            ("F", "onGeolocationPermissionsShowPrompt",
             "(Ljava/lang/String; Landroid/webkit/GeolocationPermissions/Callback;)"
  ),
        ],
        "Landroid/location/LocationManager;": [
            ("C", "GPS_PROVIDER", "Ljava/lang/String;"),
            ("C", "NETWORK_PROVIDER", "Ljava/lang/String;"),
            ("C", "PASSIVE_PROVIDER", "Ljava/lang/String;"),
            ("F", "addGpsStatusListener",
             "(Landroid/location/GpsStatus/Listener;)"),
            ("F", "addNmeaListener",
             "(Landroid/location/GpsStatus/NmeaListener;)"),
            ("F", "_requestLocationUpdates",
             "(Ljava/lang/String; J F Landroid/app/PendingIntent;)"),
            ("F", "_requestLocationUpdates",
             "(Ljava/lang/String; J F Landroid/location/LocationListener; Landroid/os/Looper;)"
  ),
            ("F", "addGpsStatusListener",
             "(Landroid/location/GpsStatus$Listener;)"),
            ("F", "addNmeaListener",
             "(Landroid/location/GpsStatus$NmeaListener;)"),
            ("F", "addProximityAlert", "(D D F J Landroid/app/PendingIntent;)"),
            ("F", "best", "(Ljava/util/List;)"),
            ("F", "getBestProvider", "(Landroid/location/Criteria; B)"),
            ("F", "getLastKnownLocation", "(Ljava/lang/String;)"),
            ("F", "getProvider", "(Ljava/lang/String;)"),
            ("F", "getProviders", "(Landroid/location/Criteria; B)"),
            ("F", "getProviders", "(B)"),
            ("F", "isProviderEnabled", "(Ljava/lang/String;)"),
            ("F", "requestLocationUpdates",
             "(Ljava/lang/String; J F Landroid/app/PendingIntent;)"),
            ("F", "requestLocationUpdates",
             "(Ljava/lang/String; J F Landroid/location/LocationListener; Landroid/os/Looper;)"
  ),
            ("F", "requestLocationUpdates",
             "(Ljava/lang/String; J F Landroid/location/LocationListener;)"),
            ("F", "sendExtraCommand",
             "(Ljava/lang/String; Ljava/lang/String; Landroid/os/Bundle;)"),
        ],
        "Landroid/webkit/GeolocationService;": [
            ("F", "registerForLocationUpdates", "()"),
            ("F", "setEnableGps", "(B)"),
            ("F", "start", "()"),
        ],
        "Landroid/telephony/TelephonyManager;": [
            ("F", "getCellLocation", "()"),
            ("F", "getCellLocation", "()"),
            ("F", "getNeighboringCellInfo", "()"),
        ],
        "Landroid/location/ILocationManager$Stub$Proxy;": [
            ("F", "addGpsStatusListener",
             "(Landroid/location/IGpsStatusListener;)"),
            ("F", "addProximityAlert", "(D D F J Landroid/app/PendingIntent;)"),
            ("F", "getLastKnownLocation", "(Ljava/lang/String;)"),
            ("F", "getProviderInfo", "(Ljava/lang/String;)"),
            ("F", "getProviders", "(B)"),
            ("F", "isProviderEnabled", "(Ljava/lang/String;)"),
            ("F", "requestLocationUpdates",
             "(Ljava/lang/String; J F Landroid/location/ILocationListener;)"),
            ("F", "requestLocationUpdatesPI",
             "(Ljava/lang/String; J F Landroid/app/PendingIntent;)"),
            ("F", "sendExtraCommand",
             "(Ljava/lang/String; Ljava/lang/String; Landroid/os/Bundle;)"),
        ],
        "Lcom/android/internal/telephony/ITelephony$Stub$Proxy;": [
            ("F", "getCellLocation", "()"),
            ("F", "getNeighboringCellInfo", "()"),
        ],
        "Landroid/webkit/GeolocationPermissions$Callback;": [
            ("F", "invok", "()"),
        ],
    },
    "READ_SMS": {
        "Landroid/provider/Telephony$Sms$Inbox;": [
            ("F", "addMessage",
             "(Landroid/content/ContentResolver; Ljava/lang/String; Ljava/lang/String; Ljava/lang/String; Ljava/lang/Long; B)"
  ),
        ],
        "Landroid/provider/Telephony$Threads;": [
            ("F", "getOrCreateThreadId",
             "(Landroid/content/Context; Ljava/lang/String;)"),
            ("F", "getOrCreateThreadId",
             "(Landroid/content/Context; Ljava/util/Set;)"),
        ],
        "Landroid/provider/Telephony$Mms;": [
            ("F", "query",
             "(Landroid/content/ContentResolver; [L[Ljava/lang/Strin; Ljava/lang/String; Ljava/lang/String;)"
  ),
            ("F", "query",
             "(Landroid/content/ContentResolver; [L[Ljava/lang/Strin;)"),
        ],
        "Landroid/provider/Telephony$Sms$Draft;": [
            ("F", "addMessage",
             "(Landroid/content/ContentResolver; Ljava/lang/String; Ljava/lang/String; Ljava/lang/String; Ljava/lang/Long;)"
  ),
        ],
        "Landroid/provider/Telephony$Sms$Sent;": [
            ("F", "addMessage",
             "(Landroid/content/ContentResolver; Ljava/lang/String; Ljava/lang/String; Ljava/lang/String; Ljava/lang/Long;)"
  ),
        ],
        "Landroid/provider/Telephony$Sms;": [
            ("F", "query",
             "(Landroid/content/ContentResolver; [L[Ljava/lang/Strin; Ljava/lang/String; Ljava/lang/String;)"
  ),
            ("F", "query",
             "(Landroid/content/ContentResolver; [L[Ljava/lang/Strin;)"),
        ],
    },
    "ACCESS_SURFACE_FLINGER": {
        "Landroid/view/SurfaceSession;": [
            ("F", "<init>", "()"),
        ],
        "Landroid/view/Surface;": [
            ("F", "closeTransaction", "()"),
            ("F", "freezeDisplay", "(I)"),
            ("F", "setOrientation", "(I I I)"),
            ("F", "setOrientation", "(I I)"),
            ("F", "unfreezeDisplay", "(I)"),
        ],
    },
    "REORDER_TASKS": {
        "Landroid/app/IActivityManager$Stub$Proxy;": [
            ("F", "moveTaskBackwards", "(I)"),
            ("F", "moveTaskToBack", "(I)"),
            ("F", "moveTaskToFront", "(I)"),
        ],
        "Landroid/app/ActivityManager;": [
            ("F", "moveTaskToFront", "(I I)"),
        ],
    },
    "MODIFY_AUDIO_SETTINGS": {
        "Landroid/net/sip/SipAudioCall;": [
            ("F", "setSpeakerMode", "(B)"),
        ],
        "Landroid/server/BluetoothA2dpService;": [
            ("F", "checkSinkSuspendState", "(I)"),
            ("F", "handleSinkStateChange",
             "(Landroid/bluetooth/BluetoothDevice;)"),
            ("F", "onBluetoothDisable", "()"),
            ("F", "onBluetoothEnable", "()"),
        ],
        "Landroid/media/IAudioService$Stub$Proxy;": [
            ("F", "setBluetoothScoOn", "(B)"),
            ("F", "setMode", "(I Landroid/os/IBinder;)"),
            ("F", "setSpeakerphoneOn", "(B)"),
            ("F", "startBluetoothSco", "(Landroid/os/IBinder;)"),
            ("F", "stopBluetoothSco", "(Landroid/os/IBinder;)"),
        ],
        "Landroid/media/AudioService;": [
            ("F", "setBluetoothScoOn", "(B)"),
            ("F", "setMode", "(I Landroid/os/IBinder;)"),
            ("F", "setSpeakerphoneOn", "(B)"),
            ("F", "startBluetoothSco", "(Landroid/os/IBinder;)"),
            ("F", "stopBluetoothSco", "(Landroid/os/IBinder;)"),
        ],
        "Landroid/media/AudioManager;": [
            ("F", "startBluetoothSco", "()"),
            ("F", "stopBluetoothSco", "()"),
            ("F", "isBluetoothA2dpOn", "()"),
            ("F", "isWiredHeadsetOn", "()"),
            ("F", "setBluetoothScoOn", "(B)"),
            ("F", "setMicrophoneMute", "(B)"),
            ("F", "setMode", "(I)"),
            ("F", "setParameter", "(Ljava/lang/String; Ljava/lang/String;)"),
            ("F", "setParameters", "(Ljava/lang/String;)"),
            ("F", "setSpeakerphoneOn", "(B)"),
            ("F", "startBluetoothSco", "()"),
            ("F", "stopBluetoothSco", "()"),
        ],
    },
    "READ_PHONE_STATE": {
        "Lcom/android/internal/telephony/IPhoneSubInfo$Stub$Proxy;": [
            ("F", "getDeviceId", "()"),
            ("F", "getDeviceSvn", "()"),
            ("F", "getIccSerialNumber", "()"),
            ("F", "getLine1AlphaTag", "()"),
            ("F", "getLine1Number", "()"),
            ("F", "getSubscriberId", "()"),
            ("F", "getVoiceMailAlphaTag", "()"),
            ("F", "getVoiceMailNumber", "()"),
        ],
        "Landroid/telephony/PhoneStateListener;": [
            ("C", "LISTEN_CALL_FORWARDING_INDICATOR", "I"),
            ("C", "LISTEN_CALL_STATE", "I"),
            ("C", "LISTEN_DATA_ACTIVITY", "I"),
            ("C", "LISTEN_MESSAGE_WAITING_INDICATOR", "I"),
            ("C", "LISTEN_SIGNAL_STRENGTH", "I"),
        ],
        "Landroid/accounts/AccountManagerService$SimWatcher;": [
            ("F", "onReceive",
             "(Landroid/content/Context; Landroid/content/Intent;)"),
        ],
        "Lcom/android/internal/telephony/CallerInfo;": [
            ("F", "markAsVoiceMail", "()"),
        ],
        "Landroid/os/Build/VERSION_CODES;": [
            ("C", "DONUT", "I"),
        ],
        "Landroid/telephony/TelephonyManager;": [
            ("C", "ACTION_PHONE_STATE_CHANGED", "Ljava/lang/String;"),
            ("F", "getDeviceId", "()"),
            ("F", "getDeviceSoftwareVersion", "()"),
            ("F", "getLine1Number", "()"),
            ("F", "getSimSerialNumber", "()"),
            ("F", "getSubscriberId", "()"),
            ("F", "getVoiceMailAlphaTag", "()"),
            ("F", "getVoiceMailNumber", "()"),
            ("F", "getDeviceId", "()"),
            ("F", "getDeviceSoftwareVersion", "()"),
            ("F", "getLine1AlphaTag", "()"),
            ("F", "getLine1Number", "()"),
            ("F", "getSimSerialNumber", "()"),
            ("F", "getSubscriberId", "()"),
            ("F", "getVoiceMailAlphaTag", "()"),
            ("F", "getVoiceMailNumber", "()"),
            ("F", "listen", "(Landroid/telephony/PhoneStateListener; I)"),
        ],
        "Lcom/android/internal/telephony/ITelephonyRegistry$Stub$Proxy;": [
            ("F", "listen",
             "(Ljava/lang/String; Lcom/android/internal/telephony/IPhoneStateListener; I B)"
  ),
        ],
        "Landroid/telephony/PhoneNumberUtils;": [
            ("F", "isVoiceMailNumber", "(Ljava/lang/String;)"),
        ],
        "Lcom/android/internal/telephony/ITelephony$Stub$Proxy;": [
            ("F", "isSimPinEnabled", "()"),
        ],
    },
    "WRITE_SETTINGS": {
        "Landroid/media/RingtoneManager;": [
            ("F", "setActualDefaultRingtoneUri",
             "(Landroid/content/Context; I Landroid/net/Uri;)"),
        ],
        "Landroid/os/IPowerManager$Stub$Proxy;": [
            ("F", "setStayOnSetting", "(I)"),
        ],
        "Landroid/server/BluetoothService;": [
            ("F", "persistBluetoothOnSetting", "(B)"),
        ],
        "Landroid/provider/Settings$Secure;": [
            ("F", "putFloat",
             "(Landroid/content/ContentResolver; Ljava/lang/String; F)"),
            ("F", "putInt",
             "(Landroid/content/ContentResolver; Ljava/lang/String; I)"),
            ("F", "putLong",
             "(Landroid/content/ContentResolver; Ljava/lang/String; J)"),
            ("F", "putString",
             "(Landroid/content/ContentResolver; Ljava/lang/String; Ljava/lang/String;)"
  ),
            ("F", "setLocationProviderEnabled",
             "(Landroid/content/ContentResolver; Ljava/lang/String; B)"),
        ],
        "Landroid/provider/Settings$Bookmarks;": [
            ("F", "add",
             "(Landroid/content/ContentResolver; Landroid/content/Intent; Ljava/lang/String; Ljava/lang/String; C I)"
  ),
            ("F", "getIntentForShortcut",
             "(Landroid/content/ContentResolver; C)"),
        ],
        "Landroid/os/IMountService$Stub$Proxy;": [
            ("F", "setAutoStartUm", "()"),
            ("F", "setPlayNotificationSound", "()"),
        ],
        "Landroid/provider/Settings$System;": [
            ("F", "putConfiguration",
             "(Landroid/content/ContentResolver; Landroid/content/res/Configuration;)"
  ),
            ("F", "putFloat",
             "(Landroid/content/ContentResolver; Ljava/lang/String; F)"),
            ("F", "putInt",
             "(Landroid/content/ContentResolver; Ljava/lang/String; I)"),
            ("F", "putLong",
             "(Landroid/content/ContentResolver; Ljava/lang/String; J)"),
            ("F", "putString",
             "(Landroid/content/ContentResolver; Ljava/lang/String; Ljava/lang/String;)"
  ),
            ("F", "setShowGTalkServiceStatus",
             "(Landroid/content/ContentResolver; B)"),
        ],
    },
    "BIND_WALLPAPER": {
        "Landroid/service/wallpaper/WallpaperService;": [
            ("C", "SERVICE_INTERFACE", "Ljava/lang/String;"),
        ],
        "Lcom/android/server/WallpaperManagerService;": [
            ("F", "bindWallpaperComponentLocked",
             "(Landroid/content/ComponentName;)"),
        ],
    },
    "DUMP": {
        "Landroid/content/ContentService;": [
            ("F", "dump",
             "(Ljava/io/FileDescriptor; Ljava/io/PrintWriter; [L[Ljava/lang/Strin;)"
  ),
        ],
        "Landroid/view/IWindowManager$Stub$Proxy;": [
            ("F", "isViewServerRunning", "()"),
            ("F", "startViewServer", "(I)"),
            ("F", "stopViewServer", "()"),
        ],
        "Landroid/os/Debug;": [
            ("F", "dumpService",
             "(Ljava/lang/String; Ljava/io/FileDescriptor; [Ljava/lang/String;)"
  ),
        ],
        "Landroid/os/IBinder;": [
            ("C", "DUMP_TRANSACTION", "I"),
        ],
        "Lcom/android/server/WallpaperManagerService;": [
            ("F", "dump",
             "(Ljava/io/FileDescriptor; Ljava/io/PrintWriter; [L[Ljava/lang/Stri;)"
  ),
        ],
    },
    "USE_CREDENTIALS": {
        "Landroid/accounts/AccountManager;": [
            ("F", "blockingGetAuthToken",
             "(Landroid/accounts/Account; Ljava/lang/String; B)"),
            ("F", "getAuthToken",
             "(Landroid/accounts/Account; Ljava/lang/String; Landroid/os/Bundle; Landroid/app/Activity; Landroid/accounts/AccountManagerCallback<android/os/Bundle>; Landroid/os/Handler;)"
  ),
            ("F", "getAuthToken",
             "(Landroid/accounts/Account; Ljava/lang/String; B Landroid/accounts/AccountManagerCallback<android/os/Bundle>; Landroid/os/Handler;)"
  ),
            ("F", "invalidateAuthToken",
             "(Ljava/lang/String; Ljava/lang/String;)"),
            ("F", "blockingGetAuthToken",
             "(Landroid/accounts/Account; Ljava/lang/String; B)"),
            ("F", "getAuthToken",
             "(Landroid/accounts/Account; Ljava/lang/String; Landroid/os/Bundle; Landroid/app/Activity; Landroid/accounts/AccountManagerCallback; Landroid/os/Handler;)"
  ),
            ("F", "getAuthToken",
             "(Landroid/accounts/Account; Ljava/lang/String; B Landroid/accounts/AccountManagerCallback; Landroid/os/Handler;)"
  ),
        ],
        "Landroid/accounts/AccountManagerService;": [
            ("F", "getAuthToken",
             "(Landroid/accounts/IAccountManagerResponse; Landroid/accounts/Account; Ljava/lang/String; B B Landroid/os/Bundle;)"
  ),
        ],
        "Landroid/accounts/IAccountManager$Stub$Proxy;": [
            ("F", "getAuthToken",
             "(Landroid/accounts/IAccountManagerResponse; Landroid/accounts/Account; Ljava/lang/String; B B Landroid/os/Bundle;)"
  ),
        ],
    },
    "UPDATE_DEVICE_STATS": {
        "Lcom/android/internal/app/IUsageStats$Stub$Proxy;": [
            ("F", "notePauseComponent", "(LComponentName;)"),
            ("F", "noteResumeComponent", "(LComponentName;)"),
        ],
        "Lcom/android/internal/app/IBatteryStats$Stub$Proxy;": [
            ("F", "noteFullWifiLockAcquired", "(I)"),
            ("F", "noteFullWifiLockReleased", "(I)"),
            ("F", "noteInputEvent", "()"),
            ("F", "notePhoneDataConnectionState", "(I B)"),
            ("F", "notePhoneOff", "()"),
            ("F", "notePhoneOn", "()"),
            ("F", "notePhoneSignalStrength", "(LSignalStrength;)"),
            ("F", "notePhoneState", "(I)"),
            ("F", "noteScanWifiLockAcquired", "(I)"),
            ("F", "noteScanWifiLockReleased", "(I)"),
            ("F", "noteScreenBrightness", "(I)"),
            ("F", "noteScreenOff", "()"),
            ("F", "noteScreenOn", "()"),
            ("F", "noteStartGps", "(I)"),
            ("F", "noteStartSensor", "(I I)"),
            ("F", "noteStartWakelock", "(I Ljava/lang/String; I)"),
            ("F", "noteStopGps", "(I)"),
            ("F", "noteStopSensor", "(I I)"),
            ("F", "noteStopWakelock", "(I Ljava/lang/String; I)"),
            ("F", "noteUserActivity", "(I I)"),
            ("F", "noteWifiMulticastDisabled", "(I)"),
            ("F", "noteWifiMulticastEnabled", "(I)"),
            ("F", "noteWifiOff", "(I)"),
            ("F", "noteWifiOn", "(I)"),
            ("F", "noteWifiRunning", "()"),
            ("F", "noteWifiStopped", "()"),
            ("F", "recordCurrentLevel", "(I)"),
            ("F", "setOnBattery", "(B I)"),
        ],
    },
    "SEND_SMS": {
        "Landroid/telephony/gsm/SmsManager;": [
            ("F", "getDefault", "()"),
            ("F", "sendDataMessage",
             "(Ljava/lang/String; Ljava/lang/String; S [B Landroid/app/PendingIntent; Landroid/app/PendingIntent;)"
  ),
            ("F", "sendTextMessage",
             "(Ljava/lang/String; Ljava/lang/String; Ljava/lang/String; Landroid/app/PendingIntent; Landroid/app/PendingIntent;)"
  ),
            ("F", "sendDataMessage",
             "(Ljava/lang/String; Ljava/lang/String; S [L; Landroid/app/PendingIntent; Landroid/app/PendingIntent;)"
  ),
            ("F", "sendMultipartTextMessage",
             "(Ljava/lang/String; Ljava/lang/String; Ljava/util/ArrayList; Ljava/util/ArrayList; Ljava/util/ArrayList;)"
  ),
            ("F", "sendTextMessage",
             "(Ljava/lang/String; Ljava/lang/String; Ljava/lang/String; Landroid/app/PendingIntent; Landroid/app/PendingIntent;)"
  ),
        ],
        "Landroid/telephony/SmsManager;": [
            ("F", "getDefault", "()"),
            ("F", "sendDataMessage",
             "(Ljava/lang/String; Ljava/lang/String; S [B Landroid/app/PendingIntent; Landroid/app/PendingIntent;)"
  ),
            ("F", "sendTextMessage",
             "(Ljava/lang/String; Ljava/lang/String; Ljava/lang/String; Landroid/app/PendingIntent; Landroid/app/PendingIntent;)"
  ),
            ("F", "sendDataMessage",
             "(Ljava/lang/String; Ljava/lang/String; S [L; Landroid/app/PendingIntent; Landroid/app/PendingIntent;)"
  ),
            ("F", "sendMultipartTextMessage",
             "(Ljava/lang/String; Ljava/lang/String; Ljava/util/ArrayList; Ljava/util/ArrayList; Ljava/util/ArrayList;)"
  ),
            ("F", "sendTextMessage",
             "(Ljava/lang/String; Ljava/lang/String; Ljava/lang/String; Landroid/app/PendingIntent; Landroid/app/PendingIntent;)"
  ),
        ],
        "Lcom/android/internal/telephony/ISms$Stub$Proxy;": [
            ("F", "sendData",
             "(Ljava/lang/String; Ljava/lang/String; I [B Landroid/app/PendingIntent; Landroid/app/PendingIntent;)"
  ),
            ("F", "sendMultipartText",
             "(Ljava/lang/String; Ljava/lang/String; Ljava/util/List; Ljava/util/List; Ljava/util/List;)"
  ),
            ("F", "sendText",
             "(Ljava/lang/String; Ljava/lang/String; Ljava/lang/String; Landroid/app/PendingIntent; Landroid/app/PendingIntent;)"
  ),
        ],
    },
    "WRITE_USER_DICTIONARY": {
        "Landroid/provider/UserDictionary$Words;": [
            ("F", "addWord",
             "(Landroid/content/Context; Ljava/lang/String; I I)"),
        ],
    },
    "ACCESS_COARSE_LOCATION": {
        "Landroid/telephony/TelephonyManager;": [
            ("F", "getCellLocation", "()"),
        ],
        "Landroid/telephony/PhoneStateListener;": [
            ("C", "LISTEN_CELL_LOCATION", "I"),
        ],
        "Landroid/location/LocationManager;": [
            ("C", "NETWORK_PROVIDER", "Ljava/lang/String;"),
        ],
    },
    "ASEC_RENAME": {
        "Landroid/os/storage/IMountService$Stub$Proxy;": [
            ("F", "renameSecureContainer",
             "(Ljava/lang/String; Ljava/lang/String;)"),
        ],
    },
    "SYSTEM_ALERT_WINDOW": {
        "Landroid/view/IWindowSession$Stub$Proxy;": [
            ("F", "add",
             "(Landroid/view/IWindow; Landroid/view/WindowManager$LayoutParams; I Landroid/graphics/Rect;)"
  ),
        ],
    },
    "CHANGE_WIFI_MULTICAST_STATE": {
        "Landroid/net/wifi/IWifiManager$Stub$Proxy;": [
            ("F", "acquireMulticastLock",
             "(Landroid/os/IBinder; Ljava/lang/String;)"),
            ("F", "initializeMulticastFiltering", "()"),
            ("F", "releaseMulticastLock", "()"),
        ],
        "Landroid/net/wifi/WifiManager$MulticastLock;": [
            ("F", "acquire", "()"),
            ("F", "finalize", "()"),
            ("F", "release", "()"),
        ],
        "Landroid/net/wifi/WifiManager;": [
            ("F", "initializeMulticastFiltering", "()"),
        ],
    },
    "RECEIVE_BOOT_COMPLETED": {
        "Landroid/content/Intent;": [
            ("C", "ACTION_BOOT_COMPLETED", "Ljava/lang/String;"),
        ],
    },
    "SET_ALARM": {
        "Landroid/provider/AlarmClock;": [
            ("C", "ACTION_SET_ALARM", "Ljava/lang/String;"),
            ("C", "EXTRA_HOUR", "Ljava/lang/String;"),
            ("C", "EXTRA_MESSAGE", "Ljava/lang/String;"),
            ("C", "EXTRA_MINUTES", "Ljava/lang/String;"),
            ("C", "EXTRA_SKIP_UI", "Ljava/lang/String;"),
        ],
    },
    "WRITE_CONTACTS": {
        "Lcom/android/internal/telephony/IccPhoneBookInterfaceManager$Stub$Proxy;":
        [
            ("F", "updateAdnRecordsInEfByIndex",
             "(I Ljava/lang/String; Ljava/lang/String; Ljava/lang/String;)"),
            ("F", "updateAdnRecordsInEfBySearch",
             "(I Ljava/lang/String; Ljava/lang/String; Ljava/lang/String; Ljava/lang/String; Ljava/lang/String;)"
  ),
        ],
        "Landroid/provider/Contacts$People;": [
            ("F", "addToGroup", "(Landroid/content/ContentResolver; J J)"),
        ],
        "Landroid/provider/ContactsContract$Contacts;": [
            ("F", "markAsContacted", "(Landroid/content/ContentResolver; J)"),
        ],
        "Landroid/provider/Contacts$Settings;": [
            ("F", "setSetting",
             "(Landroid/content/ContentResolver; Ljava/lang/String; Ljava/lang/String; Ljava/lang/String;)"
  ),
        ],
        "Lcom/android/internal/telephony/IIccPhoneBook$Stub$Proxy;": [
            ("F", "updateAdnRecordsInEfByIndex",
             "(I Ljava/lang/String; Ljava/lang/String; Ljava/lang/String;)"),
            ("F", "updateAdnRecordsInEfBySearch",
             "(I Ljava/lang/String; Ljava/lang/String; Ljava/lang/String; Ljava/lang/String; Ljava/lang/String;)"
  ),
        ],
        "Landroid/provider/CallLog$Calls;": [
            ("F", "removeExpiredEntries", "(Landroid/content/Context;)"),
        ],
        "Landroid/pim/vcard/VCardEntryCommitter;": [
            ("F", "onEntryCreated", "(Landroid/pim/vcard/VCardEntry;)"),
        ],
        "Landroid/pim/vcard/VCardEntryHandler;": [
            ("F", "onEntryCreated", "(Landroid/pim/vcard/VCardEntry;)"),
        ],
        "Landroid/pim/vcard/VCardEntry;": [
            ("F", "pushIntoContentResolver",
             "(Landroid/content/ContentResolver;)"),
        ],
    },
    "PROCESS_OUTGOING_CALLS": {
        "Landroid/content/Intent;": [
            ("C", "ACTION_NEW_OUTGOING_CALL", "Ljava/lang/String;"),
        ],
    },
    "EXPAND_STATUS_BAR": {
        "Landroid/app/StatusBarManager;": [
            ("F", "collapse", "()"),
            ("F", "expand", "()"),
            ("F", "toggle", "()"),
        ],
        "Landroid/app/IStatusBar$Stub$Proxy;": [
            ("F", "activate", "()"),
            ("F", "deactivate", "()"),
            ("F", "toggle", "()"),
        ],
    },
    "MODIFY_PHONE_STATE": {
        "Lcom/android/internal/telephony/ITelephony$Stub$Proxy;": [
            ("F", "answerRingingCall", "()"),
            ("F", "cancelMissedCallsNotification", "()"),
            ("F", "disableApnType", "(Ljava/lang/String;)"),
            ("F", "disableDataConnectivity", "()"),
            ("F", "enableApnType", "(Ljava/lang/String;)"),
            ("F", "enableDataConnectivity", "()"),
            ("F", "handlePinMmi", "(Ljava/lang/String;)"),
            ("F", "setRadio", "(B)"),
            ("F", "silenceRinger", "()"),
            ("F", "supplyPin", "(Ljava/lang/String;)"),
            ("F", "toggleRadioOnOff", "()"),
        ],
        "Landroid/net/MobileDataStateTracker;": [
            ("F", "reconnect", "()"),
            ("F", "setRadio", "(B)"),
            ("F", "teardown", "()"),
        ],
        "Lcom/android/internal/telephony/ITelephonyRegistry$Stub$Proxy;": [
            ("F", "notifyCallForwardingChanged", "(B)"),
            ("F", "notifyCallState", "(I Ljava/lang/String;)"),
            ("F", "notifyCellLocation", "(Landroid/os/Bundle;)"),
            ("F", "notifyDataActivity", "(I)"),
            ("F", "notifyDataConnection",
             "(I B Ljava/lang/String; Ljava/lang/String; [Ljava/lang/String; Ljava/lang/String; I)"
  ),
            ("F", "notifyDataConnectionFailed", "(Ljava/lang/String;)"),
            ("F", "notifyMessageWaitingChanged", "(B)"),
            ("F", "notifyServiceState", "(Landroid/telephony/ServiceState;)"),
            ("F", "notifySignalStrength", "(Landroid/telephony/SignalStrength;)"
  ),
        ],
    },
    "MOUNT_FORMAT_FILESYSTEMS": {
        "Landroid/os/IMountService$Stub$Proxy;": [
            ("F", "formatMedi", "()"),
        ],
        "Landroid/os/storage/IMountService$Stub$Proxy;": [
            ("F", "formatVolume", "(Ljava/lang/String;)"),
        ],
    },
    "ACCESS_DOWNLOAD_MANAGER": {
        "Landroid/net/Downloads$DownloadBase;": [
            ("F", "startDownloadByUri",
             "(Landroid/content/Context; Ljava/lang/String; Ljava/lang/String; B I B B Ljava/lang/String; Ljava/lang/String; Ljava/lang/String; Ljava/lang/String;)"
  ),
        ],
        "Landroid/net/Downloads$ByUri;": [
            ("F", "getCurrentOtaDownloads",
             "(Landroid/content/Context; Ljava/lang/String;)"),
            ("F", "getProgressCursor", "(Landroid/content/Context; J)"),
            ("F", "getStatus",
             "(Landroid/content/Context; Ljava/lang/String; J)"),
            ("F", "removeAllDownloadsByPackage",
             "(Landroid/content/Context; Ljava/lang/String; Ljava/lang/String;)"
  ),
            ("F", "startDownloadByUri",
             "(Landroid/content/Context; Ljava/lang/String; Ljava/lang/String; B I B B Ljava/lang/String; Ljava/lang/String; Ljava/lang/String; Ljava/lang/String;)"
  ),
        ],
        "Landroid/net/Downloads$ById;": [
            ("F", "deleteDownload", "(Landroid/content/Context; J)"),
            ("F", "getMimeTypeForId", "(Landroid/content/Context; J)"),
            ("F", "getStatus", "(Landroid/content/Context; J)"),
            ("F", "openDownload",
             "(Landroid/content/Context; J Ljava/lang/String;)"),
            ("F", "openDownloadStream", "(Landroid/content/Context; J)"),
            ("F", "startDownloadByUri",
             "(Landroid/content/Context; Ljava/lang/String; Ljava/lang/String; B I B B Ljava/lang/String; Ljava/lang/String; Ljava/lang/String; Ljava/lang/String;)"
  ),
        ],
    },
    "READ_INPUT_STATE": {
        "Landroid/view/IWindowManager$Stub$Proxy;": [
            ("F", "getDPadKeycodeState", "(I)"),
            ("F", "getDPadScancodeState", "(I)"),
            ("F", "getKeycodeState", "(I)"),
            ("F", "getKeycodeStateForDevice", "(I I)"),
            ("F", "getScancodeState", "(I)"),
            ("F", "getScancodeStateForDevice", "(I I)"),
            ("F", "getSwitchState", "(I)"),
            ("F", "getSwitchStateForDevice", "(I I)"),
            ("F", "getTrackballKeycodeState", "(I)"),
            ("F", "getTrackballScancodeState", "(I)"),
        ],
    },
    "READ_SYNC_STATS": {
        "Landroid/app/ContextImpl$ApplicationContentResolver;": [
            ("F", "getCurrentSync", "()"),
            ("F", "getSyncStatus",
             "(Landroid/accounts/Account; Ljava/lang/String;)"),
            ("F", "isSyncActive",
             "(Landroid/accounts/Account; Ljava/lang/String;)"),
            ("F", "isSyncPending",
             "(Landroid/accounts/Account; Ljava/lang/String;)"),
        ],
        "Landroid/content/ContentService;": [
            ("F", "getCurrentSync", "()"),
            ("F", "getSyncStatus",
             "(Landroid/accounts/Account; Ljava/lang/String;)"),
            ("F", "isSyncActive",
             "(Landroid/accounts/Account; Ljava/lang/String;)"),
            ("F", "isSyncPending",
             "(Landroid/accounts/Account; Ljava/lang/String;)"),
        ],
        "Landroid/content/ContentResolver;": [
            ("F", "getCurrentSync", "()"),
            ("F", "getSyncStatus",
             "(Landroid/accounts/Account; Ljava/lang/String;)"),
            ("F", "isSyncActive",
             "(Landroid/accounts/Account; Ljava/lang/String;)"),
            ("F", "isSyncPending",
             "(Landroid/accounts/Account; Ljava/lang/String;)"),
        ],
        "Landroid/content/IContentService$Stub$Proxy;": [
            ("F", "getCurrentSync", "()"),
            ("F", "getSyncStatus",
             "(Landroid/accounts/Account; Ljava/lang/String;)"),
            ("F", "isSyncActive",
             "(Landroid/accounts/Account; Ljava/lang/String;)"),
            ("F", "isSyncPending",
             "(Landroid/accounts/Account; Ljava/lang/String;)"),
        ],
    },
    "SET_TIME": {
        "Landroid/app/AlarmManager;": [
            ("F", "setTime", "(J)"),
            ("F", "setTimeZone", "(Ljava/lang/String;)"),
            ("F", "setTime", "(J)"),
        ],
        "Landroid/app/IAlarmManager$Stub$Proxy;": [
            ("F", "setTime", "(J)"),
        ],
    },
    "CHANGE_WIMAX_STATE": {
        "Lcom/htc/net/wimax/WimaxController$Stub$Proxy;": [
            ("F", "setWimaxEnable", "()"),
        ],
    },
    "MOUNT_UNMOUNT_FILESYSTEMS": {
        "Landroid/os/IMountService$Stub$Proxy;": [
            ("F", "mountMedi", "()"),
            ("F", "unmountMedi", "()"),
        ],
        "Landroid/os/storage/IMountService$Stub$Proxy;": [
            ("F", "getStorageUsers", "(Ljava/lang/String;)"),
            ("F", "mountVolume", "(Ljava/lang/String;)"),
            ("F", "setUsbMassStorageEnabled", "(B)"),
            ("F", "unmountVolume", "(Ljava/lang/String; B)"),
        ],
        "Landroid/os/storage/StorageManager;": [
            ("F", "disableUsbMassStorage", "()"),
            ("F", "enableUsbMassStorage", "()"),
        ],
    },
    "MOVE_PACKAGE": {
        "Landroid/app/ContextImpl$ApplicationPackageManager;": [
            ("F", "movePackage", "(Ljava/lang/String; LIPackageMoveObserver; I)"
  ),
            ("F", "movePackage", "(Ljava/lang/String; LIPackageMoveObserver; I)"
  ),
        ],
        "Landroid/content/pm/PackageManager;": [
            ("F", "movePackage", "(Ljava/lang/String; LIPackageMoveObserver; I)"
  ),
        ],
        "Landroid/content/pm/IPackageManager$Stub$Proxy;": [
            ("F", "movePackage",
             "(Ljava/lang/String; Landroid/content/pm/IPackageMoveObserver; I)"
  ),
        ],
    },
    "ACCESS_WIMAX_STATE": {
        "Lcom/htc/net/wimax/WimaxController$Stub$Proxy;": [
            ("F", "getConnectionInf", "()"),
            ("F", "getWimaxStat", "()"),
            ("F", "isBackoffStat", "()"),
            ("F", "isWimaxEnable", "()"),
        ],
    },
    "ACCESS_WIFI_STATE": {
        "Landroid/net/sip/SipAudioCall;": [
            ("F", "startAudio", "()"),
        ],
        "Landroid/net/wifi/IWifiManager$Stub$Proxy;": [
            ("F", "getConfiguredNetworks", "()"),
            ("F", "getConnectionInfo", "()"),
            ("F", "getDhcpInfo", "()"),
            ("F", "getNumAllowedChannels", "()"),
            ("F", "getScanResults", "()"),
            ("F", "getValidChannelCounts", "()"),
            ("F", "getWifiApEnabledState", "()"),
            ("F", "getWifiEnabledState", "()"),
            ("F", "isMulticastEnabled", "()"),
        ],
        "Landroid/net/wifi/WifiManager;": [
            ("F", "getConfiguredNetworks", "()"),
            ("F", "getConnectionInfo", "()"),
            ("F", "getDhcpInfo", "()"),
            ("F", "getNumAllowedChannels", "()"),
            ("F", "getScanResults", "()"),
            ("F", "getValidChannelCounts", "()"),
            ("F", "getWifiApState", "()"),
            ("F", "getWifiState", "()"),
            ("F", "isMulticastEnabled", "()"),
            ("F", "isWifiApEnabled", "()"),
            ("F", "isWifiEnabled", "()"),
        ],
    },
    "READ_HISTORY_BOOKMARKS": {
        "Landroid/webkit/WebIconDatabase;": [
            ("F", "bulkRequestIconForPageUrl",
             "(Landroid/content/ContentResolver; Ljava/lang/String; Landroid/webkit/WebIconDatabase$IconListener;)"
  ),
        ],
        "Landroid/provider/Browser;": [
            ("C", "BOOKMARKS_URI", "Landroid/net/Uri;"),
            ("C", "SEARCHES_URI", "Landroid/net/Uri;"),
            ("F", "addSearchUrl",
             "(Landroid/content/ContentResolver; Ljava/lang/String;)"),
            ("F", "canClearHistory", "(Landroid/content/ContentResolver;)"),
            ("F", "getAllBookmarks", "(Landroid/content/ContentResolver;)"),
            ("F", "getAllVisitedUrls", "(Landroid/content/ContentResolver;)"),
            ("F", "requestAllIcons",
             "(Landroid/content/ContentResolver; Ljava/lang/String; Landroid/webkit/WebIconDatabase/IconListener;)"
  ),
            ("F", "truncateHistory", "(Landroid/content/ContentResolver;)"),
            ("F", "updateVisitedHistory",
             "(Landroid/content/ContentResolver; Ljava/lang/String; B)"),
            ("F", "addSearchUrl",
             "(Landroid/content/ContentResolver; Ljava/lang/String;)"),
            ("F", "canClearHistory", "(Landroid/content/ContentResolver;)"),
            ("F", "clearHistory", "(Landroid/content/ContentResolver;)"),
            ("F", "deleteFromHistory",
             "(Landroid/content/ContentResolver; Ljava/lang/String;)"),
            ("F", "deleteHistoryTimeFrame",
             "(Landroid/content/ContentResolver; J J)"),
            ("F", "deleteHistoryWhere",
             "(Landroid/content/ContentResolver; Ljava/lang/String;)"),
            ("F", "getAllBookmarks", "(Landroid/content/ContentResolver;)"),
            ("F", "getAllVisitedUrls", "(Landroid/content/ContentResolver;)"),
            ("F", "getVisitedHistory", "(Landroid/content/ContentResolver;)"),
            ("F", "getVisitedLike",
             "(Landroid/content/ContentResolver; Ljava/lang/String;)"),
            ("F", "requestAllIcons",
             "(Landroid/content/ContentResolver; Ljava/lang/String; Landroid/webkit/WebIconDatabase$IconListener;)"
  ),
            ("F", "truncateHistory", "(Landroid/content/ContentResolver;)"),
            ("F", "updateVisitedHistory",
             "(Landroid/content/ContentResolver; Ljava/lang/String; B)"),
        ],
    },
    "ASEC_DESTROY": {
        "Landroid/os/storage/IMountService$Stub$Proxy;": [
            ("F", "destroySecureContainer", "(Ljava/lang/String; B)"),
        ],
    },
    "ACCESS_NETWORK_STATE": {
        "Landroid/net/ThrottleManager;": [
            ("F", "getByteCount", "(Ljava/lang/String; I I I)"),
            ("F", "getCliffLevel", "(Ljava/lang/String; I)"),
            ("F", "getCliffThreshold", "(Ljava/lang/String; I)"),
            ("F", "getHelpUri", "()"),
            ("F", "getPeriodStartTime", "(Ljava/lang/String;)"),
            ("F", "getResetTime", "(Ljava/lang/String;)"),
        ],
        "Landroid/net/NetworkInfo;": [
            ("F", "isConnectedOrConnecting", "()"),
        ],
        "Landroid/os/INetworkManagementService$Stub$Proxy;": [
            ("F", "getDnsForwarders", "()"),
            ("F", "getInterfaceRxCounter", "(Ljava/lang/String;)"),
            ("F", "getInterfaceRxThrottle", "(Ljava/lang/String;)"),
            ("F", "getInterfaceTxCounter", "(Ljava/lang/String;)"),
            ("F", "getInterfaceTxThrottle", "(Ljava/lang/String;)"),
            ("F", "getIpForwardingEnabled", "()"),
            ("F", "isTetheringStarted", "()"),
            ("F", "isUsbRNDISStarted", "()"),
            ("F", "listInterfaces", "()"),
            ("F", "listTetheredInterfaces", "()"),
            ("F", "listTtys", "()"),
        ],
        "Landroid/net/IConnectivityManager$Stub$Proxy;": [
            ("F", "getActiveNetworkInfo", "()"),
            ("F", "getAllNetworkInfo", "()"),
            ("F", "getLastTetherError", "(Ljava/lang/String;)"),
            ("F", "getMobileDataEnabled", "()"),
            ("F", "getNetworkInfo", "(I)"),
            ("F", "getNetworkPreference", "()"),
            ("F", "getTetherableIfaces", "()"),
            ("F", "getTetherableUsbRegexs", "()"),
            ("F", "getTetherableWifiRegexs", "()"),
            ("F", "getTetheredIfaces", "()"),
            ("F", "getTetheringErroredIfaces", "()"),
            ("F", "isTetheringSupported", "()"),
            ("F", "startUsingNetworkFeature",
             "(I Ljava/lang/String; Landroid/os/IBinder;)"),
        ],
        "Landroid/net/IThrottleManager$Stub$Proxy;": [
            ("F", "getByteCount", "(Ljava/lang/String; I I I)"),
            ("F", "getCliffLevel", "(Ljava/lang/String; I)"),
            ("F", "getCliffThreshold", "(Ljava/lang/String; I)"),
            ("F", "getHelpUri", "()"),
            ("F", "getPeriodStartTime", "(Ljava/lang/String;)"),
            ("F", "getResetTime", "(Ljava/lang/String;)"),
            ("F", "getThrottle", "(Ljava/lang/String;)"),
        ],
        "Landroid/net/ConnectivityManager;": [
            ("F", "getActiveNetworkInfo", "()"),
            ("F", "getAllNetworkInfo", "()"),
            ("F", "getLastTetherError", "(Ljava/lang/String;)"),
            ("F", "getMobileDataEnabled", "()"),
            ("F", "getNetworkInfo", "(I)"),
            ("F", "getNetworkPreference", "()"),
            ("F", "getTetherableIfaces", "()"),
            ("F", "getTetherableUsbRegexs", "()"),
            ("F", "getTetherableWifiRegexs", "()"),
            ("F", "getTetheredIfaces", "()"),
            ("F", "getTetheringErroredIfaces", "()"),
            ("F", "isTetheringSupported", "()"),
        ],
        "Landroid/net/http/RequestQueue;": [
            ("F", "enablePlatformNotifications", "()"),
            ("F", "setProxyConfig", "()"),
        ],
    },
    "GET_TASKS": {
        "Landroid/app/IActivityManager$Stub$Proxy;": [
            ("F", "getRecentTasks", "(I I)"),
            ("F", "getTasks", "(I I Landroid/app/IThumbnailReceiver;)"),
        ],
        "Landroid/app/ActivityManagerNative;": [
            ("F", "getRecentTasks", "(I I)"),
            ("F", "getRunningTasks", "(I)"),
        ],
        "Landroid/app/ActivityManager;": [
            ("F", "getRecentTasks", "(I I)"),
            ("F", "getRunningTasks", "(I)"),
            ("F", "getRecentTasks", "(I I)"),
            ("F", "getRunningTasks", "(I)"),
        ],
    },
    "STATUS_BAR": {
        "Landroid/view/View/OnSystemUiVisibilityChangeListener;": [
            ("F", "onSystemUiVisibilityChange", "(I)"),
        ],
        "Landroid/view/View;": [
            ("C", "STATUS_BAR_HIDDEN", "I"),
            ("C", "STATUS_BAR_VISIBLE", "I"),
        ],
        "Landroid/app/StatusBarManager;": [
            ("F", "addIcon", "(Ljava/lang/String; I I)"),
            ("F", "disable", "(I)"),
            ("F", "removeIcon", "(Landroid/os/IBinder;)"),
            ("F", "updateIcon", "(Landroid/os/IBinder; Ljava/lang/String; I I)"
  ),
        ],
        "Landroid/view/WindowManager/LayoutParams;": [
            ("C", "TYPE_STATUS_BAR", "I"),
            ("C", "TYPE_STATUS_BAR_PANEL", "I"),
            ("C", "systemUiVisibility", "I"),
            ("C", "type", "I"),
        ],
        "Landroid/app/IStatusBar$Stub$Proxy;": [
            ("F", "addIcon", "(Ljava/lang/String; Ljava/lang/String; I I)"),
            ("F", "disable", "(I Landroid/os/IBinder; Ljava/lang/String;)"),
            ("F", "removeIcon", "(Landroid/os/IBinder;)"),
            ("F", "updateIcon",
             "(Landroid/os/IBinder; Ljava/lang/String; Ljava/lang/String; I I)"
  ),
        ],
    },
    "SHUTDOWN": {
        "Landroid/app/IActivityManager$Stub$Proxy;": [
            ("F", "shutdown", "(I)"),
        ],
        "Landroid/os/IMountService$Stub$Proxy;": [
            ("F", "shutdow", "()"),
        ],
        "Landroid/os/storage/IMountService$Stub$Proxy;": [
            ("F", "shutdown", "(Landroid/os/storage/IMountShutdownObserver;)"),
        ],
        "Landroid/os/INetworkManagementService$Stub$Proxy;": [
            ("F", "shutdown", "()"),
        ],
    },
    "READ_LOGS": {
        "Landroid/os/DropBoxManager;": [
            ("C", "ACTION_DROPBOX_ENTRY_ADDED", "Ljava/lang/String;"),
            ("F", "getNextEntry", "(Ljava/lang/String; J)"),
            ("F", "getNextEntry", "(Ljava/lang/String; J)"),
        ],
        "Lcom/android/internal/os/IDropBoxManagerService$Stub$Proxy;": [
            ("F", "getNextEntry", "(Ljava/lang/String; J)"),
        ],
        "Ljava/lang/Runtime;": [
            ("F", "exec", "(Ljava/lang/String;)"),
            ("F", "exec", "([Ljava/lang/String;)"),
            ("F", "exec", "([Ljava/lang/String; [Ljava/lang/String;)"),
            ("F", "exec",
             "([Ljava/lang/String; [Ljava/lang/String; Ljava/io/File;)"),
            ("F", "exec", "(Ljava/lang/String; [Ljava/lang/String;)"),
            ("F", "exec",
             "(Ljava/lang/String; [Ljava/lang/String; Ljava/io/File;)"),
        ],
    },
    "BLUETOOTH": {
        "Landroid/os/Process;": [
            ("C", "BLUETOOTH_GID", "I"),
        ],
        "Landroid/bluetooth/BluetoothA2dp;": [
            ("C", "ACTION_CONNECTION_STATE_CHANGED", "Ljava/lang/String;"),
            ("C", "ACTION_PLAYING_STATE_CHANGED", "Ljava/lang/String;"),
            ("F", "getConnectedDevices", "()"),
            ("F", "getConnectionState", "(Landroid/bluetooth/BluetoothDevice;)"
  ),
            ("F", "getDevicesMatchingConnectionStates", "([I)"),
            ("F", "isA2dpPlaying", "(Landroid/bluetooth/BluetoothDevice;)"),
            ("F", "getConnectedSinks", "()"),
            ("F", "getNonDisconnectedSinks", "()"),
            ("F", "getSinkPriority", "(Landroid/bluetooth/BluetoothDevice;)"),
            ("F", "getSinkState", "(Landroid/bluetooth/BluetoothDevice;)"),
            ("F", "isSinkConnected", "(Landroid/bluetooth/BluetoothDevice;)"),
        ],
        "Landroid/media/AudioManager;": [
            ("C", "ROUTE_BLUETOOTH", "I"),
            ("C", "ROUTE_BLUETOOTH_A2DP", "I"),
            ("C", "ROUTE_BLUETOOTH_SCO", "I"),
        ],
        "Landroid/bluetooth/IBluetoothA2dp$Stub$Proxy;": [
            ("F", "getConnectedSinks", "()"),
            ("F", "getNonDisconnectedSinks", "()"),
            ("F", "getSinkPriority", "(Landroid/bluetooth/BluetoothDevice;)"),
            ("F", "getSinkState", "(Landroid/bluetooth/BluetoothDevice;)"),
        ],
        "Landroid/bluetooth/BluetoothSocket;": [
            ("F", "connect", "()"),
        ],
        "Landroid/bluetooth/BluetoothPbap;": [
            ("F", "getClient", "()"),
            ("F", "getState", "()"),
            ("F", "isConnected", "(Landroid/bluetooth/BluetoothDevice;)"),
        ],
        "Landroid/provider/Settings/System;": [
            ("C", "AIRPLANE_MODE_RADIOS", "Ljava/lang/String;"),
            ("C", "BLUETOOTH_DISCOVERABILITY", "Ljava/lang/String;"),
            ("C", "BLUETOOTH_DISCOVERABILITY_TIMEOUT", "Ljava/lang/String;"),
            ("C", "BLUETOOTH_ON", "Ljava/lang/String;"),
            ("C", "RADIO_BLUETOOTH", "Ljava/lang/String;"),
            ("C", "VOLUME_BLUETOOTH_SCO", "Ljava/lang/String;"),
        ],
        "Landroid/provider/Settings;": [
            ("C", "ACTION_BLUETOOTH_SETTINGS", "Ljava/lang/String;"),
        ],
        "Landroid/bluetooth/IBluetooth$Stub$Proxy;": [
            ("F", "addRfcommServiceRecord",
             "(Ljava/lang/String; Landroid/os/ParcelUuid; I Landroid/os/IBinder;)"
  ),
            ("F", "fetchRemoteUuids",
             "(Ljava/lang/String; Landroid/os/ParcelUuid; Landroid/bluetooth/IBluetoothCallback;)"
  ),
            ("F", "getAddress", "()"),
            ("F", "getBluetoothState", "()"),
            ("F", "getBondState", "(Ljava/lang/String;)"),
            ("F", "getDiscoverableTimeout", "()"),
            ("F", "getName", "()"),
            ("F", "getRemoteClass", "(Ljava/lang/String;)"),
            ("F", "getRemoteName", "(Ljava/lang/String;)"),
            ("F", "getRemoteServiceChannel",
             "(Ljava/lang/String; Landroid/os/ParcelUuid;)"),
            ("F", "getRemoteUuids", "(Ljava/lang/String;)"),
            ("F", "getScanMode", "()"),
            ("F", "getTrustState", "(Ljava/lang/String;)"),
            ("F", "isDiscovering", "()"),
            ("F", "isEnabled", "()"),
            ("F", "listBonds", "()"),
            ("F", "removeServiceRecord", "(I)"),
        ],
        "Landroid/bluetooth/BluetoothAdapter;": [
            ("C", "ACTION_CONNECTION_STATE_CHANGED", "Ljava/lang/String;"),
            ("C", "ACTION_DISCOVERY_FINISHED", "Ljava/lang/String;"),
            ("C", "ACTION_DISCOVERY_STARTED", "Ljava/lang/String;"),
            ("C", "ACTION_LOCAL_NAME_CHANGED", "Ljava/lang/String;"),
            ("C", "ACTION_REQUEST_DISCOVERABLE", "Ljava/lang/String;"),
            ("C", "ACTION_REQUEST_ENABLE", "Ljava/lang/String;"),
            ("C", "ACTION_SCAN_MODE_CHANGED", "Ljava/lang/String;"),
            ("C", "ACTION_STATE_CHANGED", "Ljava/lang/String;"),
            ("F", "cancelDiscovery", "()"),
            ("F", "disable", "()"),
            ("F", "enable", "()"),
            ("F", "getAddress", "()"),
            ("F", "getBondedDevices", "()"),
            ("F", "getName", "()"),
            ("F", "getScanMode", "()"),
            ("F", "getState", "()"),
            ("F", "isDiscovering", "()"),
            ("F", "isEnabled", "()"),
            ("F", "listenUsingInsecureRfcommWithServiceRecord",
             "(Ljava/lang/String; Ljava/util/UUID;)"),
            ("F", "listenUsingRfcommWithServiceRecord",
             "(Ljava/lang/String; Ljava/util/UUID;)"),
            ("F", "setName", "(Ljava/lang/String;)"),
            ("F", "startDiscovery", "()"),
            ("F", "getAddress", "()"),
            ("F", "getBondedDevices", "()"),
            ("F", "getDiscoverableTimeout", "()"),
            ("F", "getName", "()"),
            ("F", "getScanMode", "()"),
            ("F", "getState", "()"),
            ("F", "isDiscovering", "()"),
            ("F", "isEnabled", "()"),
            ("F", "listenUsingRfcommWithServiceRecord",
             "(Ljava/lang/String; Ljava/util/UUID;)"),
        ],
        "Landroid/bluetooth/BluetoothProfile;": [
            ("F", "getConnectedDevices", "()"),
            ("F", "getConnectionState", "(Landroid/bluetooth/BluetoothDevice;)"
  ),
            ("F", "getDevicesMatchingConnectionStates", "([I)"),
        ],
        "Landroid/bluetooth/BluetoothHeadset;": [
            ("C", "ACTION_AUDIO_STATE_CHANGED", "Ljava/lang/String;"),
            ("C", "ACTION_CONNECTION_STATE_CHANGED", "Ljava/lang/String;"),
            ("C", "ACTION_VENDOR_SPECIFIC_HEADSET_EVENT", "Ljava/lang/String;"),
            ("F", "getConnectedDevices", "()"),
            ("F", "getConnectionState", "(Landroid/bluetooth/BluetoothDevice;)"
  ),
            ("F", "getDevicesMatchingConnectionStates", "([I)"),
            ("F", "isAudioConnected", "(Landroid/bluetooth/BluetoothDevice;)"),
            ("F", "startVoiceRecognition",
             "(Landroid/bluetooth/BluetoothDevice;)"),
            ("F", "stopVoiceRecognition",
             "(Landroid/bluetooth/BluetoothDevice;)"),
            ("F", "getBatteryUsageHint", "()"),
            ("F", "getCurrentHeadset", "()"),
            ("F", "getPriority", "(Landroid/bluetooth/BluetoothDevice;)"),
            ("F", "getState", "()"),
            ("F", "isConnected", "(Landroid/bluetooth/BluetoothDevice;)"),
            ("F", "startVoiceRecognition", "()"),
            ("F", "stopVoiceRecognition", "()"),
        ],
        "Landroid/bluetooth/IBluetoothHeadset$Stub$Proxy;": [
            ("F", "getBatteryUsageHint", "()"),
            ("F", "getCurrentHeadset", "()"),
            ("F", "getPriority", "(Landroid/bluetooth/BluetoothDevice;)"),
            ("F", "getState", "()"),
            ("F", "isConnected", "(Landroid/bluetooth/BluetoothDevice;)"),
            ("F", "startVoiceRecognition", "()"),
            ("F", "stopVoiceRecognition", "()"),
        ],
        "Landroid/bluetooth/BluetoothDevice;": [
            ("C", "ACTION_ACL_CONNECTED", "Ljava/lang/String;"),
            ("C", "ACTION_ACL_DISCONNECTED", "Ljava/lang/String;"),
            ("C", "ACTION_ACL_DISCONNECT_REQUESTED", "Ljava/lang/String;"),
            ("C", "ACTION_BOND_STATE_CHANGED", "Ljava/lang/String;"),
            ("C", "ACTION_CLASS_CHANGED", "Ljava/lang/String;"),
            ("C", "ACTION_FOUND", "Ljava/lang/String;"),
            ("C", "ACTION_NAME_CHANGED", "Ljava/lang/String;"),
            ("F", "createInsecureRfcommSocketToServiceRecord",
             "(Ljava/util/UUID;)"),
            ("F", "createRfcommSocketToServiceRecord", "(Ljava/util/UUID;)"),
            ("F", "getBluetoothClass", "()"),
            ("F", "getBondState", "()"),
            ("F", "getName", "()"),
            ("F", "createRfcommSocketToServiceRecord", "(Ljava/util/UUID;)"),
            ("F", "fetchUuidsWithSdp", "()"),
            ("F", "getBondState", "()"),
            ("F", "getName", "()"),
            ("F", "getServiceChannel", "(Landroid/os/ParcelUuid;)"),
            ("F", "getUuids", "()"),
        ],
        "Landroid/server/BluetoothA2dpService;": [
            ("F", "<init>",
             "(Landroid/content/Context; Landroid/server/BluetoothService;)"),
            ("F", "addAudioSink", "(Landroid/bluetooth/BluetoothDevice;)"),
            ("F", "getConnectedSinks", "()"),
            ("F", "getNonDisconnectedSinks", "()"),
            ("F", "getSinkPriority", "(Landroid/bluetooth/BluetoothDevice;)"),
            ("F", "getSinkState", "(Landroid/bluetooth/BluetoothDevice;)"),
            ("F", "isSinkDevice", "(Landroid/bluetooth/BluetoothDevice;)"),
            ("F", "lookupSinksMatchingStates", "([I)"),
            ("F", "onConnectSinkResult", "(Ljava/lang/String; B)"),
            ("F", "onSinkPropertyChanged",
             "(Ljava/lang/String; [L[Ljava/lang/Strin;)"),
        ],
        "Landroid/provider/Settings/Secure;": [
            ("C", "BLUETOOTH_ON", "Ljava/lang/String;"),
        ],
        "Landroid/bluetooth/IBluetoothPbap$Stub$Proxy;": [
            ("F", "getClient", "()"),
            ("F", "getState", "()"),
            ("F", "isConnected", "(Landroid/bluetooth/BluetoothDevice;)"),
        ],
        "Landroid/server/BluetoothService;": [
            ("F", "addRemoteDeviceProperties",
             "(Ljava/lang/String; [L[Ljava/lang/Strin;)"),
            ("F", "addRfcommServiceRecord",
             "(Ljava/lang/String; Landroid/os/ParcelUuid; I Landroid/os/IBinder;)"
  ),
            ("F", "fetchRemoteUuids",
             "(Ljava/lang/String; Landroid/os/ParcelUuid; Landroid/bluetooth/IBluetoothCallback;)"
  ),
            ("F", "getAddress", "()"),
            ("F", "getAddressFromObjectPath", "(Ljava/lang/String;)"),
            ("F", "getAllProperties", "()"),
            ("F", "getBluetoothState", "()"),
            ("F", "getBondState", "(Ljava/lang/String;)"),
            ("F", "getDiscoverableTimeout", "()"),
            ("F", "getName", "()"),
            ("F", "getObjectPathFromAddress", "(Ljava/lang/String;)"),
            ("F", "getProperty", "(Ljava/lang/String;)"),
            ("F", "getPropertyInternal", "(Ljava/lang/String;)"),
            ("F", "getRemoteClass", "(Ljava/lang/String;)"),
            ("F", "getRemoteName", "(Ljava/lang/String;)"),
            ("F", "getRemoteServiceChannel",
             "(Ljava/lang/String; Landroid/os/ParcelUuid;)"),
            ("F", "getRemoteUuids", "(Ljava/lang/String;)"),
            ("F", "getScanMode", "()"),
            ("F", "getTrustState", "(Ljava/lang/String;)"),
            ("F", "isDiscovering", "()"),
            ("F", "isEnabled", "()"),
            ("F", "listBonds", "()"),
            ("F", "removeServiceRecord", "(I)"),
            ("F", "sendUuidIntent", "(Ljava/lang/String;)"),
            ("F", "setLinkTimeout", "(Ljava/lang/String; I)"),
            ("F", "setPropertyBoolean", "(Ljava/lang/String; B)"),
            ("F", "setPropertyInteger", "(Ljava/lang/String; I)"),
            ("F", "setPropertyString", "(Ljava/lang/String; Ljava/lang/String;)"
  ),
            ("F", "updateDeviceServiceChannelCache", "(Ljava/lang/String;)"),
            ("F", "updateRemoteDevicePropertiesCache", "(Ljava/lang/String;)"),
        ],
        "Landroid/content/pm/PackageManager;": [
            ("C", "FEATURE_BLUETOOTH", "Ljava/lang/String;"),
        ],
        "Landroid/bluetooth/BluetoothAssignedNumbers;": [
            ("C", "BLUETOOTH_SIG", "I"),
        ],
    },
    "CLEAR_APP_USER_DATA": {
        "Landroid/app/ActivityManagerNative;": [
            ("F", "clearApplicationUserData",
             "(Ljava/lang/String; Landroid/content/pm/IPackageDataObserver;)"),
        ],
        "Landroid/app/ContextImpl$ApplicationPackageManager;": [
            ("F", "clearApplicationUserData",
             "(Ljava/lang/String; LIPackageDataObserver;)"),
            ("F", "clearApplicationUserData",
             "(Ljava/lang/String; LIPackageDataObserver;)"),
        ],
        "Landroid/app/ActivityManager;": [
            ("F", "clearApplicationUserData",
             "(Ljava/lang/String; Landroid/content/pm/IPackageDataObserver;)"),
        ],
        "Landroid/app/IActivityManager$Stub$Proxy;": [
            ("F", "clearApplicationUserData",
             "(Ljava/lang/String; Landroid/content/pm/IPackageDataObserver;)"),
        ],
        "Landroid/content/pm/PackageManager;": [
            ("F", "clearApplicationUserData",
             "(Ljava/lang/String; LIPackageDataObserver;)"),
        ],
        "Landroid/content/pm/IPackageManager$Stub$Proxy;": [
            ("F", "clearApplicationUserData",
             "(Ljava/lang/String; Landroid/content/pm/IPackageDataObserver;)"),
        ],
    },
    "WRITE_SMS": {
        "Landroid/provider/Telephony$Sms;": [
            ("F", "addMessageToUri",
             "(Landroid/content/ContentResolver; Landroid/net/Uri; Ljava/lang/String; Ljava/lang/String; Ljava/lang/String; Ljava/lang/Long; B B J)"
  ),
            ("F", "addMessageToUri",
             "(Landroid/content/ContentResolver; Landroid/net/Uri; Ljava/lang/String; Ljava/lang/String; Ljava/lang/String; Ljava/lang/Long; B B)"
  ),
            ("F", "moveMessageToFolder",
             "(Landroid/content/Context; Landroid/net/Uri; I I)"),
        ],
        "Landroid/provider/Telephony$Sms$Outbox;": [
            ("F", "addMessage",
             "(Landroid/content/ContentResolver; Ljava/lang/String; Ljava/lang/String; Ljava/lang/String; Ljava/lang/Long; B J)"
  ),
        ],
        "Landroid/provider/Telephony$Sms$Draft;": [
            ("F", "saveMessage",
             "(Landroid/content/ContentResolver; Landroid/net/Uri; Ljava/lang/String;)"
  ),
        ],
    },
    "SET_PROCESS_LIMIT": {
        "Landroid/app/IActivityManager$Stub$Proxy;": [
            ("F", "setProcessForeground", "(Landroid/os/IBinder; I B)"),
            ("F", "setProcessLimit", "(I)"),
        ],
    },
    "DEVICE_POWER": {
        "Landroid/os/PowerManager;": [
            ("F", "goToSleep", "(J)"),
            ("F", "setBacklightBrightness", "(I)"),
        ],
        "Landroid/os/IPowerManager$Stub$Proxy;": [
            ("F", "clearUserActivityTimeout", "(J J)"),
            ("F", "goToSleep", "(J)"),
            ("F", "goToSleepWithReason", "(J I)"),
            ("F", "preventScreenOn", "(B)"),
            ("F", "setAttentionLight", "(B I)"),
            ("F", "setBacklightBrightness", "(I)"),
            ("F", "setPokeLock", "(I Landroid/os/IBinder; Ljava/lang/String;)"),
            ("F", "userActivityWithForce", "(J B B)"),
        ],
    },
    "PERSISTENT_ACTIVITY": {
        "Landroid/app/ExpandableListActivity;": [
            ("F", "setPersistent", "(B)"),
        ],
        "Landroid/accounts/GrantCredentialsPermissionActivity;": [
            ("F", "setPersistent", "(B)"),
        ],
        "Landroid/app/Activity;": [
            ("F", "setPersistent", "(B)"),
        ],
        "Landroid/app/ListActivity;": [
            ("F", "setPersistent", "(B)"),
        ],
        "Landroid/app/AliasActivity;": [
            ("F", "setPersistent", "(B)"),
        ],
        "Landroid/accounts/AccountAuthenticatorActivity;": [
            ("F", "setPersistent", "(B)"),
        ],
        "Landroid/app/IActivityManager$Stub$Proxy;": [
            ("F", "setPersistent", "(Landroid/os/IBinder; B)"),
        ],
        "Landroid/app/TabActivity;": [
            ("F", "setPersistent", "(B)"),
        ],
        "Landroid/app/ActivityGroup;": [
            ("F", "setPersistent", "(B)"),
        ],
    },
    "MANAGE_APP_TOKENS": {
        "Landroid/view/IWindowManager$Stub$Proxy;": [
            ("F", "addAppToken", "(I Landroid/view/IApplicationToken; I I B)"),
            ("F", "addWindowToken", "(Landroid/os/IBinder; I)"),
            ("F", "executeAppTransition", "()"),
            ("F", "moveAppToken", "(I Landroid/os/IBinder;)"),
            ("F", "moveAppTokensToBottom", "(Ljava/util/List;)"),
            ("F", "moveAppTokensToTop", "(Ljava/util/List;)"),
            ("F", "pauseKeyDispatching", "(Landroid/os/IBinder;)"),
            ("F", "prepareAppTransition", "(I)"),
            ("F", "removeAppToken", "(Landroid/os/IBinder;)"),
            ("F", "removeWindowToken", "(Landroid/os/IBinder;)"),
            ("F", "resumeKeyDispatching", "(Landroid/os/IBinder;)"),
            ("F", "setAppGroupId", "(Landroid/os/IBinder; I)"),
            ("F", "setAppOrientation", "(Landroid/view/IApplicationToken; I)"),
            ("F", "setAppStartingWindow",
             "(Landroid/os/IBinder; Ljava/lang/String; I Ljava/lang/CharSequence; I I Landroid/os/IBinder; B)"
  ),
            ("F", "setAppVisibility", "(Landroid/os/IBinder; B)"),
            ("F", "setAppWillBeHidden", "(Landroid/os/IBinder;)"),
            ("F", "setEventDispatching", "(B)"),
            ("F", "setFocusedApp", "(Landroid/os/IBinder; B)"),
            ("F", "setNewConfiguration", "(Landroid/content/res/Configuration;)"
  ),
            ("F", "startAppFreezingScreen", "(Landroid/os/IBinder; I)"),
            ("F", "stopAppFreezingScreen", "(Landroid/os/IBinder; B)"),
            ("F", "updateOrientationFromAppTokens",
             "(Landroid/content/res/Configuration; Landroid/os/IBinder;)"),
        ],
    },
    "WRITE_HISTORY_BOOKMARKS": {
        "Landroid/provider/Browser;": [
            ("C", "BOOKMARKS_URI", "Landroid/net/Uri;"),
            ("C", "SEARCHES_URI", "Landroid/net/Uri;"),
            ("F", "addSearchUrl",
             "(Landroid/content/ContentResolver; Ljava/lang/String;)"),
            ("F", "clearHistory", "(Landroid/content/ContentResolver;)"),
            ("F", "clearSearches", "(Landroid/content/ContentResolver;)"),
            ("F", "deleteFromHistory",
             "(Landroid/content/ContentResolver; Ljava/lang/String;)"),
            ("F", "deleteHistoryTimeFrame",
             "(Landroid/content/ContentResolver; J J)"),
            ("F", "truncateHistory", "(Landroid/content/ContentResolver;)"),
            ("F", "updateVisitedHistory",
             "(Landroid/content/ContentResolver; Ljava/lang/String; B)"),
            ("F", "clearSearches", "(Landroid/content/ContentResolver;)"),
        ],
    },
    "FORCE_BACK": {
        "Landroid/app/IActivityManager$Stub$Proxy;": [
            ("F", "unhandledBack", "(I)"),
        ],
    },
    "CHANGE_NETWORK_STATE": {
        "Landroid/net/IConnectivityManager$Stub$Proxy;": [
            ("F", "requestRouteToHost", "(I I)"),
            ("F", "setMobileDataEnabled", "(B)"),
            ("F", "setNetworkPreference", "(I)"),
            ("F", "setRadio", "(I B)"),
            ("F", "setRadios", "(B)"),
            ("F", "stopUsingNetworkFeature", "(I Ljava/lang/String;)"),
            ("F", "tether", "(Ljava/lang/String;)"),
            ("F", "untether", "(Ljava/lang/String;)"),
        ],
        "Landroid/net/ConnectivityManager;": [
            ("F", "requestRouteToHost", "(I I)"),
            ("F", "setMobileDataEnabled", "(B)"),
            ("F", "setNetworkPreference", "(I)"),
            ("F", "setRadio", "(I B)"),
            ("F", "setRadios", "(B)"),
            ("F", "startUsingNetworkFeature", "(I Ljava/lang/String;)"),
            ("F", "stopUsingNetworkFeature", "(I Ljava/lang/String;)"),
            ("F", "tether", "(Ljava/lang/String;)"),
            ("F", "untether", "(Ljava/lang/String;)"),
        ],
        "Landroid/os/INetworkManagementService$Stub$Proxy;": [
            ("F", "attachPppd",
             "(Ljava/lang/String; Ljava/lang/String; Ljava/lang/String; Ljava/lang/String; Ljava/lang/String;)"
  ),
            ("F", "detachPppd", "(Ljava/lang/String;)"),
            ("F", "disableNat", "(Ljava/lang/String; Ljava/lang/String;)"),
            ("F", "enableNat", "(Ljava/lang/String; Ljava/lang/String;)"),
            ("F", "setAccessPoint",
             "(Landroid/net/wifi/WifiConfiguration; Ljava/lang/String; Ljava/lang/String;)"
  ),
            ("F", "setInterfaceThrottle", "(Ljava/lang/String; I I)"),
            ("F", "setIpForwardingEnabled", "(B)"),
            ("F", "startAccessPoint",
             "(Landroid/net/wifi/WifiConfiguration; Ljava/lang/String; Ljava/lang/String;)"
  ),
            ("F", "startUsbRNDIS", "()"),
            ("F", "stopAccessPoint", "()"),
            ("F", "stopTethering", "()"),
            ("F", "stopUsbRNDIS", "()"),
            ("F", "tetherInterface", "(Ljava/lang/String;)"),
            ("F", "unregisterObserver",
             "(Landroid/net/INetworkManagementEventObserver;)"),
            ("F", "untetherInterface", "(Ljava/lang/String;)"),
        ],
    },
    "WRITE_SYNC_SETTINGS": {
        "Landroid/app/ContextImpl$ApplicationContentResolver;": [
            ("F", "addPeriodicSync",
             "(Landroid/accounts/Account; Ljava/lang/String; Landroid/os/Bundle; J)"
  ),
            ("F", "removePeriodicSync",
             "(Landroid/accounts/Account; Ljava/lang/String; Landroid/os/Bundle;)"
  ),
            ("F", "setIsSyncable",
             "(Landroid/accounts/Account; Ljava/lang/String; I)"),
            ("F", "setMasterSyncAutomatically", "(B)"),
            ("F", "setSyncAutomatically",
             "(Landroid/accounts/Account; Ljava/lang/String; B)"),
        ],
        "Landroid/content/ContentService;": [
            ("F", "addPeriodicSync",
             "(Landroid/accounts/Account; Ljava/lang/String; Landroid/os/Bundle; J)"
  ),
            ("F", "removePeriodicSync",
             "(Landroid/accounts/Account; Ljava/lang/String; Landroid/os/Bundle;)"
  ),
            ("F", "setIsSyncable",
             "(Landroid/accounts/Account; Ljava/lang/String; I)"),
            ("F", "setMasterSyncAutomatically", "(B)"),
            ("F", "setSyncAutomatically",
             "(Landroid/accounts/Account; Ljava/lang/String; B)"),
        ],
        "Landroid/content/ContentResolver;": [
            ("F", "addPeriodicSync",
             "(Landroid/accounts/Account; Ljava/lang/String; Landroid/os/Bundle; J)"
  ),
            ("F", "removePeriodicSync",
             "(Landroid/accounts/Account; Ljava/lang/String; Landroid/os/Bundle;)"
  ),
            ("F", "setIsSyncable",
             "(Landroid/accounts/Account; Ljava/lang/String; I)"),
            ("F", "setMasterSyncAutomatically", "(B)"),
            ("F", "setSyncAutomatically",
             "(Landroid/accounts/Account; Ljava/lang/String; B)"),
        ],
        "Landroid/content/IContentService$Stub$Proxy;": [
            ("F", "addPeriodicSync",
             "(Landroid/accounts/Account; Ljava/lang/String; Landroid/os/Bundle; J)"
  ),
            ("F", "removePeriodicSync",
             "(Landroid/accounts/Account; Ljava/lang/String; Landroid/os/Bundle;)"
  ),
            ("F", "setIsSyncable",
             "(Landroid/accounts/Account; Ljava/lang/String; I)"),
            ("F", "setMasterSyncAutomatically", "(B)"),
            ("F", "setSyncAutomatically",
             "(Landroid/accounts/Account; Ljava/lang/String; B)"),
        ],
    },
    "ACCOUNT_MANAGER": {
        "Landroid/accounts/AccountManager;": [
            ("C", "KEY_ACCOUNT_MANAGER_RESPONSE", "Ljava/lang/String;"),
        ],
        "Landroid/accounts/AbstractAccountAuthenticator;": [
            ("F", "checkBinderPermission", "()"),
            ("F", "confirmCredentials",
             "(Landroid/accounts/IAccountAuthenticatorResponse; Landroid/accounts/Account; Landroid/os/Bundle;)"
  ),
            ("F", "editProperties",
             "(Landroid/accounts/IAccountAuthenticatorResponse; Ljava/lang/String;)"
  ),
            ("F", "getAccountRemovalAllowed",
             "(Landroid/accounts/IAccountAuthenticatorResponse; Landroid/accounts/Account;)"
  ),
            ("F", "getAuthToken",
             "(Landroid/accounts/IAccountAuthenticatorResponse; Landroid/accounts/Account; Ljava/lang/String; Landroid/os/Bundle;)"
  ),
            ("F", "getAuthTokenLabel",
             "(Landroid/accounts/IAccountAuthenticatorResponse; Ljava/lang/String;)"
  ),
            ("F", "hasFeatures",
             "(Landroid/accounts/IAccountAuthenticatorResponse; Landroid/accounts/Account; [L[Ljava/lang/Strin;)"
  ),
            ("F", "updateCredentials",
             "(Landroid/accounts/IAccountAuthenticatorResponse; Landroid/accounts/Account; Ljava/lang/String; Landroid/os/Bundle;)"
  ),
            ("F", "addAccount",
             "(Landroid/accounts/IAccountAuthenticatorResponse; Ljava/lang/String; Ljava/lang/String; [L[Ljava/lang/Strin; Landroid/os/Bundle;)"
  ),
        ],
        "Landroid/accounts/AbstractAccountAuthenticator$Transport;": [
            ("F", "addAccount",
             "(Landroid/accounts/IAccountAuthenticatorResponse; Ljava/lang/String; Ljava/lang/String; [L[Ljava/lang/Strin; Landroid/os/Bundle;)"
  ),
            ("F", "confirmCredentials",
             "(Landroid/accounts/IAccountAuthenticatorResponse; Landroid/accounts/Account; Landroid/os/Bundle;)"
  ),
            ("F", "editProperties",
             "(Landroid/accounts/IAccountAuthenticatorResponse; Ljava/lang/String;)"
  ),
            ("F", "getAccountRemovalAllowed",
             "(Landroid/accounts/IAccountAuthenticatorResponse; Landroid/accounts/Account;)"
  ),
            ("F", "getAuthToken",
             "(Landroid/accounts/IAccountAuthenticatorResponse; Landroid/accounts/Account; Ljava/lang/String; Landroid/os/Bundle;)"
  ),
            ("F", "getAuthTokenLabel",
             "(Landroid/accounts/IAccountAuthenticatorResponse; Ljava/lang/String;)"
  ),
            ("F", "hasFeatures",
             "(Landroid/accounts/IAccountAuthenticatorResponse; Landroid/accounts/Account; [L[Ljava/lang/Strin;)"
  ),
            ("F", "updateCredentials",
             "(Landroid/accounts/IAccountAuthenticatorResponse; Landroid/accounts/Account; Ljava/lang/String; Landroid/os/Bundle;)"
  ),
        ],
        "Landroid/accounts/IAccountAuthenticator$Stub$Proxy;": [
            ("F", "addAccount",
             "(Landroid/accounts/IAccountAuthenticatorResponse; Ljava/lang/String; Ljava/lang/String; [L[Ljava/lang/Strin; Landroid/os/Bundle;)"
  ),
            ("F", "confirmCredentials",
             "(Landroid/accounts/IAccountAuthenticatorResponse; Landroid/accounts/Account; Landroid/os/Bundle;)"
  ),
            ("F", "editProperties",
             "(Landroid/accounts/IAccountAuthenticatorResponse; Ljava/lang/String;)"
  ),
            ("F", "getAccountRemovalAllowed",
             "(Landroid/accounts/IAccountAuthenticatorResponse; Landroid/accounts/Account;)"
  ),
            ("F", "getAuthToken",
             "(Landroid/accounts/IAccountAuthenticatorResponse; Landroid/accounts/Account; Ljava/lang/String; Landroid/os/Bundle;)"
  ),
            ("F", "getAuthTokenLabel",
             "(Landroid/accounts/IAccountAuthenticatorResponse; Ljava/lang/String;)"
  ),
            ("F", "hasFeatures",
             "(Landroid/accounts/IAccountAuthenticatorResponse; Landroid/accounts/Account; [L[Ljava/lang/Strin;)"
  ),
            ("F", "updateCredentials",
             "(Landroid/accounts/IAccountAuthenticatorResponse; Landroid/accounts/Account; Ljava/lang/String; Landroid/os/Bundle;)"
  ),
        ],
    },
    "SET_ANIMATION_SCALE": {
        "Landroid/view/IWindowManager$Stub$Proxy;": [
            ("F", "setAnimationScale", "(I F)"),
            ("F", "setAnimationScales", "([L;)"),
        ],
    },
    "GET_ACCOUNTS": {
        "Landroid/accounts/AccountManager;": [
            ("F", "getAccounts", "()"),
            ("F", "getAccountsByType", "(Ljava/lang/String;)"),
            ("F", "getAccountsByTypeAndFeatures",
             "(Ljava/lang/String; [Ljava/lang/String; [Landroid/accounts/AccountManagerCallback<android/accounts/Account[; Landroid/os/Handler;)"
  ),
            ("F", "hasFeatures",
             "(Landroid/accounts/Account; [Ljava/lang/String; Landroid/accounts/AccountManagerCallback<java/lang/Boolean>; Landroid/os/Handler;)"
  ),
            ("F", "addOnAccountsUpdatedListener",
             "(Landroid/accounts/OnAccountsUpdateListener; Landroid/os/Handler; B)"
  ),
            ("F", "getAccounts", "()"),
            ("F", "getAccountsByType", "(Ljava/lang/String;)"),
            ("F", "getAccountsByTypeAndFeatures",
             "(Ljava/lang/String; [L[Ljava/lang/Strin; Landroid/accounts/AccountManagerCallback; Landroid/os/Handler;)"
  ),
            ("F", "getAuthTokenByFeatures",
             "(Ljava/lang/String; Ljava/lang/String; [L[Ljava/lang/Strin; Landroid/app/Activity; Landroid/os/Bundle; Landroid/os/Bundle; Landroid/accounts/AccountManagerCallback; Landroid/os/Handler;)"
  ),
            ("F", "hasFeatures",
             "(Landroid/accounts/Account; [L[Ljava/lang/Strin; Landroid/accounts/AccountManagerCallback; Landroid/os/Handler;)"
  ),
        ],
        "Landroid/content/ContentService;": [
            ("F", "<init>", "(Landroid/content/Context; B)"),
            ("F", "main", "(Landroid/content/Context; B)"),
        ],
        "Landroid/accounts/AccountManager$GetAuthTokenByTypeAndFeaturesTask;": [
            ("F", "doWork", "()"),
            ("F", "start", "()"),
        ],
        "Landroid/accounts/AccountManager$AmsTask;": [
            ("F", "doWork", "()"),
            ("F", "start", "()"),
        ],
        "Landroid/accounts/IAccountManager$Stub$Proxy;": [
            ("F", "getAccounts", "(Ljava/lang/String;)"),
            ("F", "getAccountsByFeatures",
             "(Landroid/accounts/IAccountManagerResponse; Ljava/lang/String; [L[Ljava/lang/Strin;)"
  ),
            ("F", "hasFeatures",
             "(Landroid/accounts/IAccountManagerResponse; Landroid/accounts/Account; [L[Ljava/lang/Strin;)"
  ),
        ],
        "Landroid/accounts/AccountManagerService;": [
            ("F", "checkReadAccountsPermission", "()"),
            ("F", "getAccounts", "(Ljava/lang/String;)"),
            ("F", "getAccountsByFeatures",
             "(Landroid/accounts/IAccountManagerResponse; Ljava/lang/String; [L[Ljava/lang/Strin;)"
  ),
            ("F", "hasFeatures",
             "(Landroid/accounts/IAccountManagerResponse; Landroid/accounts/Account; [L[Ljava/lang/Strin;)"
  ),
        ],
    },
    "RECEIVE_SMS": {
        "Landroid/telephony/gsm/SmsManager;": [
            ("F", "copyMessageToSim", "([L; [L; I)"),
            ("F", "deleteMessageFromSim", "(I)"),
            ("F", "getAllMessagesFromSim", "()"),
            ("F", "updateMessageOnSim", "(I I [L;)"),
        ],
        "Landroid/telephony/SmsManager;": [
            ("F", "copyMessageToIcc", "([L; [L; I)"),
            ("F", "deleteMessageFromIcc", "(I)"),
            ("F", "getAllMessagesFromIcc", "()"),
            ("F", "updateMessageOnIcc", "(I I [L;)"),
        ],
        "Lcom/android/internal/telephony/ISms$Stub$Proxy;": [
            ("F", "copyMessageToIccEf", "(I [B [B)"),
            ("F", "getAllMessagesFromIccEf", "()"),
            ("F", "updateMessageOnIccEf", "(I I [B)"),
        ],
    },
    "STOP_APP_SWITCHES": {
        "Landroid/app/IActivityManager$Stub$Proxy;": [
            ("F", "resumeAppSwitches", "()"),
            ("F", "stopAppSwitches", "()"),
        ],
    },
    "DELETE_CACHE_FILES": {
        "Landroid/app/ContextImpl$ApplicationPackageManager;": [
            ("F", "deleteApplicationCacheFiles",
             "(Ljava/lang/String; LIPackageDataObserver;)"),
            ("F", "deleteApplicationCacheFiles",
             "(Ljava/lang/String; Landroid/content/pm/IPackageDataObserver;)"),
        ],
        "Landroid/content/pm/PackageManager;": [
            ("F", "deleteApplicationCacheFiles",
             "(Ljava/lang/String; Landroid/content/pm/IPackageDataObserver;)"),
        ],
        "Landroid/content/pm/IPackageManager$Stub$Proxy;": [
            ("F", "deleteApplicationCacheFiles",
             "(Ljava/lang/String; Landroid/content/pm/IPackageDataObserver;)"),
        ],
    },
    "WRITE_EXTERNAL_STORAGE": {
        "Landroid/os/Build/VERSION_CODES;": [
            ("C", "DONUT", "I"),
        ],
        "Landroid/app/DownloadManager/Request;": [
            ("F", "setDestinationUri", "(Landroid/net/Uri;)"),
        ],
    },
    "REBOOT": {
        "Landroid/os/RecoverySystem;": [
            ("F", "installPackage", "(Landroid/content/Context; Ljava/io/File;)"
  ),
            ("F", "rebootWipeUserData", "(Landroid/content/Context;)"),
            ("F", "bootCommand",
             "(Landroid/content/Context; Ljava/lang/String;)"),
            ("F", "installPackage", "(Landroid/content/Context; Ljava/io/File;)"
  ),
            ("F", "rebootWipeUserData", "(Landroid/content/Context;)"),
        ],
        "Landroid/content/Intent;": [
            ("C", "IntentResolution", "Ljava/lang/String;"),
            ("C", "ACTION_REBOOT", "Ljava/lang/String;"),
        ],
        "Landroid/os/PowerManager;": [
            ("F", "reboot", "(Ljava/lang/String;)"),
            ("F", "reboot", "(Ljava/lang/String;)"),
        ],
        "Landroid/os/IPowerManager$Stub$Proxy;": [
            ("F", "crash", "(Ljava/lang/String;)"),
            ("F", "reboot", "(Ljava/lang/String;)"),
        ],
    },
    "INSTALL_PACKAGES": {
        "Landroid/app/ContextImpl$ApplicationPackageManager;": [
            ("F", "installPackage",
             "(Landroid/net/Uri; LIPackageInstallObserver; I Ljava/lang/String;)"
  ),
            ("F", "installPackage",
             "(Landroid/net/Uri; LIPackageInstallObserver; I Ljava/lang/String;)"
  ),
        ],
        "Landroid/content/pm/PackageManager;": [
            ("F", "installPackage",
             "(Landroid/net/Uri; LIPackageInstallObserver; I Ljava/lang/String;)"
  ),
        ],
        "Landroid/content/pm/IPackageManager$Stub$Proxy;": [
            ("F", "installPackage",
             "(Landroid/net/Uri; Landroid/content/pm/IPackageInstallObserver; I Ljava/lang/String;)"
  ),
        ],
    },
    "SET_DEBUG_APP": {
        "Landroid/app/IActivityManager$Stub$Proxy;": [
            ("F", "setDebugApp", "(Ljava/lang/String; B B)"),
        ],
    },
    "INSTALL_LOCATION_PROVIDER": {
        "Landroid/location/ILocationManager$Stub$Proxy;": [
            ("F", "reportLocation", "(Landroid/location/Location; B)"),
        ],
    },
    "SET_WALLPAPER_HINTS": {
        "Landroid/app/WallpaperManager;": [
            ("F", "suggestDesiredDimensions", "(I I)"),
        ],
        "Landroid/app/IWallpaperManager$Stub$Proxy;": [
            ("F", "setDimensionHints", "(I I)"),
        ],
    },
    "READ_CONTACTS": {
        "Landroid/app/ContextImpl$ApplicationContentResolver;": [
            ("F", "openFileDescriptor", "(Landroid/net/Uri; Ljava/lang/String;)"
  ),
            ("F", "openInputStream", "(Landroid/net/Uri;)"),
            ("F", "openOutputStream", "(Landroid/net/Uri;)"),
            ("F", "query",
             "(Landroid/net/Uri; [L[Ljava/lang/Strin; Ljava/lang/String; [L[Ljava/lang/Strin; Ljava/lang/String;)"
  ),
        ],
        "Lcom/android/internal/telephony/IccPhoneBookInterfaceManager$Stub$Proxy;":
        [
            ("F", "getAdnRecordsInEf", "(I)"),
        ],
        "Landroid/provider/Contacts$People;": [
            ("F", "addToGroup",
             "(Landroid/content/ContentResolver; J Ljava/lang/String;)"),
            ("F", "addToMyContactsGroup",
             "(Landroid/content/ContentResolver; J)"),
            ("F", "createPersonInMyContactsGroup",
             "(Landroid/content/ContentResolver; Landroid/content/ContentValues;)"
  ),
            ("F", "loadContactPhoto",
             "(Landroid/content/Context; Landroid/net/Uri; I Landroid/graphics/BitmapFactory$Options;)"
  ),
            ("F", "markAsContacted", "(Landroid/content/ContentResolver; J)"),
            ("F", "openContactPhotoInputStream",
             "(Landroid/content/ContentResolver; Landroid/net/Uri;)"),
            ("F", "queryGroups", "(Landroid/content/ContentResolver; J)"),
            ("F", "setPhotoData",
             "(Landroid/content/ContentResolver; Landroid/net/Uri; [L;)"),
            ("F", "tryGetMyContactsGroupId",
             "(Landroid/content/ContentResolver;)"),
        ],
        "Landroid/provider/ContactsContract$Data;": [
            ("F", "getContactLookupUri",
             "(Landroid/content/ContentResolver; Landroid/net/Uri;)"),
        ],
        "Landroid/provider/ContactsContract$Contacts;": [
            ("F", "getLookupUri",
             "(Landroid/content/ContentResolver; Landroid/net/Uri;)"),
            ("F", "lookupContact",
             "(Landroid/content/ContentResolver; Landroid/net/Uri;)"),
            ("F", "openContactPhotoInputStream",
             "(Landroid/content/ContentResolver; Landroid/net/Uri;)"),
        ],
        "Landroid/pim/vcard/VCardComposer;": [
            ("F", "createOneEntry", "()"),
            ("F", "createOneEntry", "(Ljava/lang/reflect/Method;)"),
            ("F", "createOneEntryInternal",
             "(Ljava/lang/String; Ljava/lang/reflect/Method;)"),
            ("F", "init", "()"),
            ("F", "init", "(Ljava/lang/String; [L[Ljava/lang/Strin;)"),
        ],
        "Landroid/pim/vcard/VCardComposer$OneEntryHandler;": [
            ("F", "onInit", "(Landroid/content/Context;)"),
        ],
        "Lcom/android/internal/telephony/CallerInfo;": [
            ("F", "getCallerId",
             "(Landroid/content/Context; Ljava/lang/String;)"),
            ("F", "getCallerInfo",
             "(Landroid/content/Context; Ljava/lang/String;)"),
        ],
        "Landroid/provider/Contacts$Settings;": [
            ("F", "getSetting",
             "(Landroid/content/ContentResolver; Ljava/lang/String; Ljava/lang/String;)"
  ),
        ],
        "Landroid/provider/ContactsContract$RawContacts;": [
            ("F", "getContactLookupUri",
             "(Landroid/content/ContentResolver; Landroid/net/Uri;)"),
        ],
        "Landroid/provider/CallLog$Calls;": [
            ("F", "addCall",
             "(Lcom/android/internal/telephony/CallerInfo; Landroid/content/Context; Ljava/lang/String; I I J I)"
  ),
            ("F", "getLastOutgoingCall", "(Landroid/content/Context;)"),
        ],
        "Lcom/android/internal/telephony/IIccPhoneBook$Stub$Proxy;": [
            ("F", "getAdnRecordsInEf", "(I)"),
        ],
        "Landroid/pim/vcard/VCardComposer$HandlerForOutputStream;": [
            ("F", "onInit", "(Landroid/content/Context;)"),
        ],
        "Landroid/provider/ContactsContract$CommonDataKinds$Phone;": [
            ("C", "CONTENT_URI", "Landroid/net/Uri;"),
        ],
        "Landroid/widget/QuickContactBadge;": [
            ("F", "assignContactFromEmail", "(Ljava/lang/String; B)"),
            ("F", "assignContactFromPhone", "(Ljava/lang/String; B)"),
            ("F", "trigger", "(Landroid/net/Uri;)"),
        ],
        "Landroid/content/ContentResolver;": [
            ("F", "openFileDescriptor", "(Landroid/net/Uri; Ljava/lang/String;)"
  ),
            ("F", "openInputStream", "(Landroid/net/Uri;)"),
            ("F", "openOutputStream", "(Landroid/net/Uri;)"),
            ("F", "query",
             "(Landroid/net/Uri; [L[Ljava/lang/Strin; Ljava/lang/String; [L[Ljava/lang/Strin; Ljava/lang/String;)"
  ),
        ],
    },
    "BACKUP": {
        "Landroid/app/backup/IBackupManager$Stub$Proxy;": [
            ("F", "backupNow", "()"),
            ("F", "beginRestoreSession", "(Ljava/lang/String;)"),
            ("F", "clearBackupData", "(Ljava/lang/String;)"),
            ("F", "dataChanged", "(Ljava/lang/String;)"),
            ("F", "getCurrentTransport", "()"),
            ("F", "isBackupEnabled", "()"),
            ("F", "listAllTransports", "()"),
            ("F", "selectBackupTransport", "(Ljava/lang/String;)"),
            ("F", "setAutoRestore", "(B)"),
            ("F", "setBackupEnabled", "(B)"),
        ],
        "Landroid/app/IActivityManager$Stub$Proxy;": [
            ("F", "bindBackupAgent", "(Landroid/content/pm/ApplicationInfo; I)"
  ),
        ],
        "Landroid/app/backup/BackupManager;": [
            ("F", "beginRestoreSession", "()"),
            ("F", "dataChanged", "(Ljava/lang/String;)"),
            ("F", "requestRestore", "(Landroid/app/backup/RestoreObserver;)"),
        ],
    },
}

DVM_PERMISSIONS_BY_ELEMENT = {
    "Landroid/app/admin/DeviceAdminReceiver;-ACTION_DEVICE_ADMIN_ENABLED-Ljava/lang/String;":
    "BIND_DEVICE_ADMIN",
    "Landroid/app/admin/DevicePolicyManager;-getRemoveWarning-(Landroid/content/ComponentName; Landroid/os/RemoteCallback;)":
    "BIND_DEVICE_ADMIN",
    "Landroid/app/admin/DevicePolicyManager;-reportFailedPasswordAttempt-()":
    "BIND_DEVICE_ADMIN",
    "Landroid/app/admin/DevicePolicyManager;-reportSuccessfulPasswordAttempt-()":
    "BIND_DEVICE_ADMIN",
    "Landroid/app/admin/DevicePolicyManager;-setActiveAdmin-(Landroid/content/ComponentName;)":
    "BIND_DEVICE_ADMIN",
    "Landroid/app/admin/DevicePolicyManager;-setActivePasswordState-(I I)":
    "BIND_DEVICE_ADMIN",
    "Landroid/app/admin/IDevicePolicyManager$Stub$Proxy;-getRemoveWarning-(Landroid/content/ComponentName; Landroid/os/RemoteCallback;)":
    "BIND_DEVICE_ADMIN",
    "Landroid/app/admin/IDevicePolicyManager$Stub$Proxy;-reportFailedPasswordAttempt-()":
    "BIND_DEVICE_ADMIN",
    "Landroid/app/admin/IDevicePolicyManager$Stub$Proxy;-reportSuccessfulPasswordAttempt-()":
    "BIND_DEVICE_ADMIN",
    "Landroid/app/admin/IDevicePolicyManager$Stub$Proxy;-setActiveAdmin-(Landroid/content/ComponentName;)":
    "BIND_DEVICE_ADMIN",
    "Landroid/app/admin/IDevicePolicyManager$Stub$Proxy;-setActivePasswordState-(I I)":
    "BIND_DEVICE_ADMIN",
    "Landroid/app/ContextImpl$ApplicationContentResolver;-getIsSyncable-(Landroid/accounts/Account; Ljava/lang/String;)":
    "READ_SYNC_SETTINGS",
    "Landroid/app/ContextImpl$ApplicationContentResolver;-getMasterSyncAutomatically-()":
    "READ_SYNC_SETTINGS",
    "Landroid/app/ContextImpl$ApplicationContentResolver;-getPeriodicSyncs-(Landroid/accounts/Account; Ljava/lang/String;)":
    "READ_SYNC_SETTINGS",
    "Landroid/app/ContextImpl$ApplicationContentResolver;-getSyncAutomatically-(Landroid/accounts/Account; Ljava/lang/String;)":
    "READ_SYNC_SETTINGS",
    "Landroid/content/ContentService;-getIsSyncable-(Landroid/accounts/Account; Ljava/lang/String;)":
    "READ_SYNC_SETTINGS",
    "Landroid/content/ContentService;-getMasterSyncAutomatically-()":
    "READ_SYNC_SETTINGS",
    "Landroid/content/ContentService;-getPeriodicSyncs-(Landroid/accounts/Account; Ljava/lang/String;)":
    "READ_SYNC_SETTINGS",
    "Landroid/content/ContentService;-getSyncAutomatically-(Landroid/accounts/Account; Ljava/lang/String;)":
    "READ_SYNC_SETTINGS",
    "Landroid/content/ContentResolver;-getIsSyncable-(Landroid/accounts/Account; Ljava/lang/String;)":
    "READ_SYNC_SETTINGS",
    "Landroid/content/ContentResolver;-getMasterSyncAutomatically-()":
    "READ_SYNC_SETTINGS",
    "Landroid/content/ContentResolver;-getPeriodicSyncs-(Landroid/accounts/Account; Ljava/lang/String;)":
    "READ_SYNC_SETTINGS",
    "Landroid/content/ContentResolver;-getSyncAutomatically-(Landroid/accounts/Account; Ljava/lang/String;)":
    "READ_SYNC_SETTINGS",
    "Landroid/content/IContentService$Stub$Proxy;-getIsSyncable-(Landroid/accounts/Account; Ljava/lang/String;)":
    "READ_SYNC_SETTINGS",
    "Landroid/content/IContentService$Stub$Proxy;-getMasterSyncAutomatically-()":
    "READ_SYNC_SETTINGS",
    "Landroid/content/IContentService$Stub$Proxy;-getPeriodicSyncs-(Landroid/accounts/Account; Ljava/lang/String;)":
    "READ_SYNC_SETTINGS",
    "Landroid/content/IContentService$Stub$Proxy;-getSyncAutomatically-(Landroid/accounts/Account; Ljava/lang/String;)":
    "READ_SYNC_SETTINGS",
    "Landroid/content/pm/ApplicationInfo;-FLAG_FACTORY_TEST-I": "FACTORY_TEST",
    "Landroid/content/pm/ApplicationInfo;-flags-I": "FACTORY_TEST",
    "Landroid/content/Intent;-IntentResolution-Ljava/lang/String;":
    "FACTORY_TEST",
    "Landroid/content/Intent;-ACTION_FACTORY_TEST-Ljava/lang/String;":
    "FACTORY_TEST",
    "Landroid/app/IActivityManager$Stub$Proxy;-setAlwaysFinish-(B)":
    "SET_ALWAYS_FINISH",
    "Landroid/provider/Calendar$CalendarAlerts;-alarmExists-(Landroid/content/ContentResolver; J J J)":
    "READ_CALENDAR",
    "Landroid/provider/Calendar$CalendarAlerts;-findNextAlarmTime-(Landroid/content/ContentResolver; J)":
    "READ_CALENDAR",
    "Landroid/provider/Calendar$CalendarAlerts;-query-(Landroid/content/ContentResolver; [L[Ljava/lang/Strin; Ljava/lang/String; [L[Ljava/lang/Strin; Ljava/lang/String;)":
    "READ_CALENDAR",
    "Landroid/provider/Calendar$Calendars;-query-(Landroid/content/ContentResolver; [L[Ljava/lang/Strin; Ljava/lang/String; Ljava/lang/String;)":
    "READ_CALENDAR",
    "Landroid/provider/Calendar$Events;-query-(Landroid/content/ContentResolver; [L[Ljava/lang/Strin; Ljava/lang/String; Ljava/lang/String;)":
    "READ_CALENDAR",
    "Landroid/provider/Calendar$Events;-query-(Landroid/content/ContentResolver; [L[Ljava/lang/Strin;)":
    "READ_CALENDAR",
    "Landroid/provider/Calendar$Instances;-query-(Landroid/content/ContentResolver; [L[Ljava/lang/Strin; J J Ljava/lang/String; Ljava/lang/String;)":
    "READ_CALENDAR",
    "Landroid/provider/Calendar$Instances;-query-(Landroid/content/ContentResolver; [L[Ljava/lang/Strin; J J)":
    "READ_CALENDAR",
    "Landroid/provider/Calendar$EventDays;-query-(Landroid/content/ContentResolver; I I)":
    "READ_CALENDAR",
    "Landroid/provider/DrmStore;-enforceAccessDrmPermission-(Landroid/content/Context;)":
    "ACCESS_DRM",
    "Landroid/app/IActivityManager$Stub$Proxy;-updateConfiguration-(Landroid/content/res/Configuration;)":
    "CHANGE_CONFIGURATION",
    "Landroid/app/IActivityManager$Stub$Proxy;-profileControl-(Ljava/lang/String; B Ljava/lang/String; Landroid/os/ParcelFileDescriptor;)":
    "SET_ACTIVITY_WATCHER",
    "Landroid/app/IActivityManager$Stub$Proxy;-setActivityController-(Landroid/app/IActivityController;)":
    "SET_ACTIVITY_WATCHER",
    "Landroid/app/ContextImpl$ApplicationPackageManager;-getPackageSizeInfo-(Ljava/lang/String; LIPackageStatsObserver;)":
    "GET_PACKAGE_SIZE",
    "Landroid/app/ContextImpl$ApplicationPackageManager;-getPackageSizeInfo-(Ljava/lang/String; Landroid/content/pm/IPackageStatsObserver;)":
    "GET_PACKAGE_SIZE",
    "Landroid/content/pm/PackageManager;-getPackageSizeInfo-(Ljava/lang/String; Landroid/content/pm/IPackageStatsObserver;)":
    "GET_PACKAGE_SIZE",
    "Landroid/telephony/TelephonyManager;-disableLocationUpdates-()":
    "CONTROL_LOCATION_UPDATES",
    "Landroid/telephony/TelephonyManager;-enableLocationUpdates-()":
    "CONTROL_LOCATION_UPDATES",
    "Lcom/android/internal/telephony/ITelephony$Stub$Proxy;-disableLocationUpdates-()":
    "CONTROL_LOCATION_UPDATES",
    "Lcom/android/internal/telephony/ITelephony$Stub$Proxy;-enableLocationUpdates-()":
    "CONTROL_LOCATION_UPDATES",
    "Landroid/app/ContextImpl$ApplicationPackageManager;-freeStorage-(J LIntentSender;)":
    "CLEAR_APP_CACHE",
    "Landroid/app/ContextImpl$ApplicationPackageManager;-freeStorageAndNotify-(J LIPackageDataObserver;)":
    "CLEAR_APP_CACHE",
    "Landroid/app/ContextImpl$ApplicationPackageManager;-freeStorage-(J Landroid/content/IntentSender;)":
    "CLEAR_APP_CACHE",
    "Landroid/app/ContextImpl$ApplicationPackageManager;-freeStorageAndNotify-(J Landroid/content/pm/IPackageDataObserver;)":
    "CLEAR_APP_CACHE",
    "Landroid/content/pm/PackageManager;-freeStorage-(J Landroid/content/IntentSender;)":
    "CLEAR_APP_CACHE",
    "Landroid/content/pm/PackageManager;-freeStorageAndNotify-(J Landroid/content/pm/IPackageDataObserver;)":
    "CLEAR_APP_CACHE",
    "Landroid/content/pm/IPackageManager$Stub$Proxy;-freeStorage-(J Landroid/content/IntentSender;)":
    "CLEAR_APP_CACHE",
    "Landroid/content/pm/IPackageManager$Stub$Proxy;-freeStorageAndNotify-(J Landroid/content/pm/IPackageDataObserver;)":
    "CLEAR_APP_CACHE",
    "Landroid/view/inputmethod/InputMethod;-SERVICE_INTERFACE-Ljava/lang/String;":
    "BIND_INPUT_METHOD",
    "Landroid/app/IActivityManager$Stub$Proxy;-signalPersistentProcesses-(I)":
    "SIGNAL_PERSISTENT_PROCESSES",
    "Lcom/android/internal/app/IBatteryStats$Stub$Proxy;-getAwakeTimeBattery-()":
    "BATTERY_STATS",
    "Lcom/android/internal/app/IBatteryStats$Stub$Proxy;-getAwakeTimePlugged-()":
    "BATTERY_STATS",
    "Lcom/android/internal/app/IBatteryStats$Stub$Proxy;-getStatistics-()":
    "BATTERY_STATS",
    "Landroid/accounts/AccountManager;-addAccountExplicitly-(Landroid/accounts/Account; Ljava/lang/String; Landroid/os/Bundle;)":
    "AUTHENTICATE_ACCOUNTS",
    "Landroid/accounts/AccountManager;-getPassword-(Landroid/accounts/Account;)":
    "AUTHENTICATE_ACCOUNTS",
    "Landroid/accounts/AccountManager;-getUserData-(Landroid/accounts/Account; Ljava/lang/String;)":
    "AUTHENTICATE_ACCOUNTS",
    "Landroid/accounts/AccountManager;-peekAuthToken-(Landroid/accounts/Account; Ljava/lang/String;)":
    "AUTHENTICATE_ACCOUNTS",
    "Landroid/accounts/AccountManager;-setAuthToken-(Landroid/accounts/Account; Ljava/lang/String; Ljava/lang/String;)":
    "AUTHENTICATE_ACCOUNTS",
    "Landroid/accounts/AccountManager;-setPassword-(Landroid/accounts/Account; Ljava/lang/String;)":
    "AUTHENTICATE_ACCOUNTS",
    "Landroid/accounts/AccountManager;-setUserData-(Landroid/accounts/Account; Ljava/lang/String; Ljava/lang/String;)":
    "AUTHENTICATE_ACCOUNTS",
    "Landroid/accounts/AccountManager;-addAccountExplicitly-(Landroid/accounts/Account; Ljava/lang/String; Landroid/os/Bundle;)":
    "AUTHENTICATE_ACCOUNTS",
    "Landroid/accounts/AccountManager;-getPassword-(Landroid/accounts/Account;)":
    "AUTHENTICATE_ACCOUNTS",
    "Landroid/accounts/AccountManager;-getUserData-(Landroid/accounts/Account; Ljava/lang/String;)":
    "AUTHENTICATE_ACCOUNTS",
    "Landroid/accounts/AccountManager;-peekAuthToken-(Landroid/accounts/Account; Ljava/lang/String;)":
    "AUTHENTICATE_ACCOUNTS",
    "Landroid/accounts/AccountManager;-setAuthToken-(Landroid/accounts/Account; Ljava/lang/String; Ljava/lang/String;)":
    "AUTHENTICATE_ACCOUNTS",
    "Landroid/accounts/AccountManager;-setPassword-(Landroid/accounts/Account; Ljava/lang/String;)":
    "AUTHENTICATE_ACCOUNTS",
    "Landroid/accounts/AccountManager;-setUserData-(Landroid/accounts/Account; Ljava/lang/String; Ljava/lang/String;)":
    "AUTHENTICATE_ACCOUNTS",
    "Landroid/accounts/AccountManagerService;-addAccount-(Landroid/accounts/Account; Ljava/lang/String; Landroid/os/Bundle;)":
    "AUTHENTICATE_ACCOUNTS",
    "Landroid/accounts/AccountManagerService;-checkAuthenticateAccountsPermission-(Landroid/accounts/Account;)":
    "AUTHENTICATE_ACCOUNTS",
    "Landroid/accounts/AccountManagerService;-getPassword-(Landroid/accounts/Account;)":
    "AUTHENTICATE_ACCOUNTS",
    "Landroid/accounts/AccountManagerService;-getUserData-(Landroid/accounts/Account; Ljava/lang/String;)":
    "AUTHENTICATE_ACCOUNTS",
    "Landroid/accounts/AccountManagerService;-peekAuthToken-(Landroid/accounts/Account; Ljava/lang/String;)":
    "AUTHENTICATE_ACCOUNTS",
    "Landroid/accounts/AccountManagerService;-setAuthToken-(Landroid/accounts/Account; Ljava/lang/String; Ljava/lang/String;)":
    "AUTHENTICATE_ACCOUNTS",
    "Landroid/accounts/AccountManagerService;-setPassword-(Landroid/accounts/Account; Ljava/lang/String;)":
    "AUTHENTICATE_ACCOUNTS",
    "Landroid/accounts/AccountManagerService;-setUserData-(Landroid/accounts/Account; Ljava/lang/String; Ljava/lang/String;)":
    "AUTHENTICATE_ACCOUNTS",
    "Landroid/accounts/IAccountManager$Stub$Proxy;-addAccount-(Landroid/accounts/Account; Ljava/lang/String; Landroid/os/Bundle;)":
    "AUTHENTICATE_ACCOUNTS",
    "Landroid/accounts/IAccountManager$Stub$Proxy;-getPassword-(Landroid/accounts/Account;)":
    "AUTHENTICATE_ACCOUNTS",
    "Landroid/accounts/IAccountManager$Stub$Proxy;-getUserData-(Landroid/accounts/Account; Ljava/lang/String;)":
    "AUTHENTICATE_ACCOUNTS",
    "Landroid/accounts/IAccountManager$Stub$Proxy;-peekAuthToken-(Landroid/accounts/Account; Ljava/lang/String;)":
    "AUTHENTICATE_ACCOUNTS",
    "Landroid/accounts/IAccountManager$Stub$Proxy;-setAuthToken-(Landroid/accounts/Account; Ljava/lang/String; Ljava/lang/String;)":
    "AUTHENTICATE_ACCOUNTS",
    "Landroid/accounts/IAccountManager$Stub$Proxy;-setPassword-(Landroid/accounts/Account; Ljava/lang/String;)":
    "AUTHENTICATE_ACCOUNTS",
    "Landroid/accounts/IAccountManager$Stub$Proxy;-setUserData-(Landroid/accounts/Account; Ljava/lang/String; Ljava/lang/String;)":
    "AUTHENTICATE_ACCOUNTS",
    "Landroid/net/IConnectivityManager$Stub$Proxy;-setBackgroundDataSetting-(B)":
    "CHANGE_BACKGROUND_DATA_SETTING",
    "Landroid/net/ConnectivityManager;-setBackgroundDataSetting-(B)":
    "CHANGE_BACKGROUND_DATA_SETTING",
    "Landroid/app/ActivityManagerNative;-killBackgroundProcesses-(Ljava/lang/String;)":
    "RESTART_PACKAGES",
    "Landroid/app/ActivityManagerNative;-restartPackage-(Ljava/lang/String;)":
    "RESTART_PACKAGES",
    "Landroid/app/ActivityManager;-killBackgroundProcesses-(Ljava/lang/String;)":
    "RESTART_PACKAGES",
    "Landroid/app/ActivityManager;-restartPackage-(Ljava/lang/String;)":
    "RESTART_PACKAGES",
    "Landroid/telephony/TelephonyManager;-getCompleteVoiceMailNumber-()":
    "CALL_PRIVILEGED",
    "Landroid/telephony/PhoneNumberUtils;-getNumberFromIntent-(Landroid/content/Intent; Landroid/content/Context;)":
    "CALL_PRIVILEGED",
    "Landroid/app/IWallpaperManager$Stub$Proxy;-setWallpaperComponent-(Landroid/content/ComponentName;)":
    "SET_WALLPAPER_COMPONENT",
    "Landroid/view/IWindowManager$Stub$Proxy;-disableKeyguard-(Landroid/os/IBinder; Ljava/lang/String;)":
    "DISABLE_KEYGUARD",
    "Landroid/view/IWindowManager$Stub$Proxy;-exitKeyguardSecurely-(Landroid/view/IOnKeyguardExitResult;)":
    "DISABLE_KEYGUARD",
    "Landroid/view/IWindowManager$Stub$Proxy;-reenableKeyguard-(Landroid/os/IBinder;)":
    "DISABLE_KEYGUARD",
    "Landroid/app/KeyguardManager;-exitKeyguardSecurely-(Landroid/app/KeyguardManager$OnKeyguardExitResult;)":
    "DISABLE_KEYGUARD",
    "Landroid/app/KeyguardManager$KeyguardLock;-disableKeyguard-()":
    "DISABLE_KEYGUARD",
    "Landroid/app/KeyguardManager$KeyguardLock;-reenableKeyguard-()":
    "DISABLE_KEYGUARD",
    "Landroid/app/ContextImpl$ApplicationPackageManager;-deletePackage-(Ljava/lang/String; LIPackageDeleteObserver; I)":
    "DELETE_PACKAGES",
    "Landroid/app/ContextImpl$ApplicationPackageManager;-deletePackage-(Ljava/lang/String; LIPackageDeleteObserver; I)":
    "DELETE_PACKAGES",
    "Landroid/content/pm/PackageManager;-deletePackage-(Ljava/lang/String; LIPackageDeleteObserver; I)":
    "DELETE_PACKAGES",
    "Landroid/content/pm/IPackageManager$Stub$Proxy;-deletePackage-(Ljava/lang/String; Landroid/content/pm/IPackageDeleteObserver; I)":
    "DELETE_PACKAGES",
    "Landroid/app/ContextImpl$ApplicationPackageManager;-setApplicationEnabledSetting-(Ljava/lang/String; I I)":
    "CHANGE_COMPONENT_ENABLED_STATE",
    "Landroid/app/ContextImpl$ApplicationPackageManager;-setComponentEnabledSetting-(LComponentName; I I)":
    "CHANGE_COMPONENT_ENABLED_STATE",
    "Landroid/app/ContextImpl$ApplicationPackageManager;-setApplicationEnabledSetting-(Ljava/lang/String; I I)":
    "CHANGE_COMPONENT_ENABLED_STATE",
    "Landroid/app/ContextImpl$ApplicationPackageManager;-setComponentEnabledSetting-(Landroid/content/ComponentName; I I)":
    "CHANGE_COMPONENT_ENABLED_STATE",
    "Landroid/content/pm/PackageManager;-setApplicationEnabledSetting-(Ljava/lang/String; I I)":
    "CHANGE_COMPONENT_ENABLED_STATE",
    "Landroid/content/pm/PackageManager;-setComponentEnabledSetting-(Landroid/content/ComponentName; I I)":
    "CHANGE_COMPONENT_ENABLED_STATE",
    "Landroid/content/pm/IPackageManager$Stub$Proxy;-setApplicationEnabledSetting-(Ljava/lang/String; I I)":
    "CHANGE_COMPONENT_ENABLED_STATE",
    "Landroid/content/pm/IPackageManager$Stub$Proxy;-setComponentEnabledSetting-(Landroid/content/ComponentName; I I)":
    "CHANGE_COMPONENT_ENABLED_STATE",
    "Landroid/os/storage/IMountService$Stub$Proxy;-getSecureContainerList-()":
    "ASEC_ACCESS",
    "Landroid/os/storage/IMountService$Stub$Proxy;-getSecureContainerPath-(Ljava/lang/String;)":
    "ASEC_ACCESS",
    "Landroid/os/storage/IMountService$Stub$Proxy;-isSecureContainerMounted-(Ljava/lang/String;)":
    "ASEC_ACCESS",
    "Lcom/android/internal/app/IUsageStats$Stub$Proxy;-noteLaunchTime-(LComponentName;)":
    "UPDATE_DEVICE_STATS",
    "Landroid/net/sip/SipAudioCall;-startAudio-()": "RECORD_AUDIO",
    "Landroid/media/MediaRecorder;-setAudioSource-(I)": "RECORD_AUDIO",
    "Landroid/speech/SpeechRecognizer;-cancel-()": "RECORD_AUDIO",
    "Landroid/speech/SpeechRecognizer;-handleCancelMessage-()": "RECORD_AUDIO",
    "Landroid/speech/SpeechRecognizer;-handleStartListening-(Landroid/content/Intent;)":
    "RECORD_AUDIO",
    "Landroid/speech/SpeechRecognizer;-handleStopMessage-()": "RECORD_AUDIO",
    "Landroid/speech/SpeechRecognizer;-startListening-(Landroid/content/Intent;)":
    "RECORD_AUDIO",
    "Landroid/speech/SpeechRecognizer;-stopListening-()": "RECORD_AUDIO",
    "Landroid/media/AudioRecord;-<init>-(I I I I I)": "RECORD_AUDIO",
    "Landroid/location/LocationManager;-addTestProvider-(Ljava/lang/String; B B B B B B B I I)":
    "ACCESS_MOCK_LOCATION",
    "Landroid/location/LocationManager;-clearTestProviderEnabled-(Ljava/lang/String;)":
    "ACCESS_MOCK_LOCATION",
    "Landroid/location/LocationManager;-clearTestProviderLocation-(Ljava/lang/String;)":
    "ACCESS_MOCK_LOCATION",
    "Landroid/location/LocationManager;-clearTestProviderStatus-(Ljava/lang/String;)":
    "ACCESS_MOCK_LOCATION",
    "Landroid/location/LocationManager;-removeTestProvider-(Ljava/lang/String;)":
    "ACCESS_MOCK_LOCATION",
    "Landroid/location/LocationManager;-setTestProviderEnabled-(Ljava/lang/String; B)":
    "ACCESS_MOCK_LOCATION",
    "Landroid/location/LocationManager;-setTestProviderLocation-(Ljava/lang/String; Landroid/location/Location;)":
    "ACCESS_MOCK_LOCATION",
    "Landroid/location/LocationManager;-setTestProviderStatus-(Ljava/lang/String; I Landroid/os/Bundle; J)":
    "ACCESS_MOCK_LOCATION",
    "Landroid/location/LocationManager;-addTestProvider-(Ljava/lang/String; B B B B B B B I I)":
    "ACCESS_MOCK_LOCATION",
    "Landroid/location/LocationManager;-clearTestProviderEnabled-(Ljava/lang/String;)":
    "ACCESS_MOCK_LOCATION",
    "Landroid/location/LocationManager;-clearTestProviderLocation-(Ljava/lang/String;)":
    "ACCESS_MOCK_LOCATION",
    "Landroid/location/LocationManager;-clearTestProviderStatus-(Ljava/lang/String;)":
    "ACCESS_MOCK_LOCATION",
    "Landroid/location/LocationManager;-removeTestProvider-(Ljava/lang/String;)":
    "ACCESS_MOCK_LOCATION",
    "Landroid/location/LocationManager;-setTestProviderEnabled-(Ljava/lang/String; B)":
    "ACCESS_MOCK_LOCATION",
    "Landroid/location/LocationManager;-setTestProviderLocation-(Ljava/lang/String; Landroid/location/Location;)":
    "ACCESS_MOCK_LOCATION",
    "Landroid/location/LocationManager;-setTestProviderStatus-(Ljava/lang/String; I Landroid/os/Bundle; J)":
    "ACCESS_MOCK_LOCATION",
    "Landroid/location/ILocationManager$Stub$Proxy;-addTestProvider-(Ljava/lang/String; B B B B B B B I I)":
    "ACCESS_MOCK_LOCATION",
    "Landroid/location/ILocationManager$Stub$Proxy;-clearTestProviderEnabled-(Ljava/lang/String;)":
    "ACCESS_MOCK_LOCATION",
    "Landroid/location/ILocationManager$Stub$Proxy;-clearTestProviderLocation-(Ljava/lang/String;)":
    "ACCESS_MOCK_LOCATION",
    "Landroid/location/ILocationManager$Stub$Proxy;-clearTestProviderStatus-(Ljava/lang/String;)":
    "ACCESS_MOCK_LOCATION",
    "Landroid/location/ILocationManager$Stub$Proxy;-removeTestProvider-(Ljava/lang/String;)":
    "ACCESS_MOCK_LOCATION",
    "Landroid/location/ILocationManager$Stub$Proxy;-setTestProviderEnabled-(Ljava/lang/String; B)":
    "ACCESS_MOCK_LOCATION",
    "Landroid/location/ILocationManager$Stub$Proxy;-setTestProviderLocation-(Ljava/lang/String; Landroid/location/Location;)":
    "ACCESS_MOCK_LOCATION",
    "Landroid/location/ILocationManager$Stub$Proxy;-setTestProviderStatus-(Ljava/lang/String; I Landroid/os/Bundle; J)":
    "ACCESS_MOCK_LOCATION",
    "Landroid/media/AudioManager;-EXTRA_RINGER_MODE-Ljava/lang/String;":
    "VIBRATE",
    "Landroid/media/AudioManager;-EXTRA_VIBRATE_SETTING-Ljava/lang/String;":
    "VIBRATE",
    "Landroid/media/AudioManager;-EXTRA_VIBRATE_TYPE-Ljava/lang/String;":
    "VIBRATE",
    "Landroid/media/AudioManager;-FLAG_REMOVE_SOUND_AND_VIBRATE-I": "VIBRATE",
    "Landroid/media/AudioManager;-FLAG_VIBRATE-I": "VIBRATE",
    "Landroid/media/AudioManager;-RINGER_MODE_VIBRATE-I": "VIBRATE",
    "Landroid/media/AudioManager;-VIBRATE_SETTING_CHANGED_ACTION-Ljava/lang/String;":
    "VIBRATE",
    "Landroid/media/AudioManager;-VIBRATE_SETTING_OFF-I": "VIBRATE",
    "Landroid/media/AudioManager;-VIBRATE_SETTING_ON-I": "VIBRATE",
    "Landroid/media/AudioManager;-VIBRATE_SETTING_ONLY_SILENT-I": "VIBRATE",
    "Landroid/media/AudioManager;-VIBRATE_TYPE_NOTIFICATION-I": "VIBRATE",
    "Landroid/media/AudioManager;-VIBRATE_TYPE_RINGER-I": "VIBRATE",
    "Landroid/media/AudioManager;-getRingerMode-()": "VIBRATE",
    "Landroid/media/AudioManager;-getVibrateSetting-(I)": "VIBRATE",
    "Landroid/media/AudioManager;-setRingerMode-(I)": "VIBRATE",
    "Landroid/media/AudioManager;-setVibrateSetting-(I I)": "VIBRATE",
    "Landroid/media/AudioManager;-shouldVibrate-(I)": "VIBRATE",
    "Landroid/os/Vibrator;-cancel-()": "VIBRATE",
    "Landroid/os/Vibrator;-vibrate-([L; I)": "VIBRATE",
    "Landroid/os/Vibrator;-vibrate-(J)": "VIBRATE",
    "Landroid/provider/Settings/System;-VIBRATE_ON-Ljava/lang/String;": "VIBRATE",
    "Landroid/app/NotificationManager;-notify-(I Landroid/app/Notification;)":
    "VIBRATE",
    "Landroid/app/NotificationManager;-notify-(Ljava/lang/String; I Landroid/app/Notification;)":
    "VIBRATE",
    "Landroid/app/Notification/Builder;-setDefaults-(I)": "VIBRATE",
    "Landroid/os/IVibratorService$Stub$Proxy;-cancelVibrate-(Landroid/os/IBinder;)":
    "VIBRATE",
    "Landroid/os/IVibratorService$Stub$Proxy;-vibrate-(J Landroid/os/IBinder;)":
    "VIBRATE",
    "Landroid/os/IVibratorService$Stub$Proxy;-vibratePattern-([L; I Landroid/os/IBinder;)":
    "VIBRATE",
    "Landroid/app/Notification;-DEFAULT_VIBRATE-I": "VIBRATE",
    "Landroid/app/Notification;-defaults-I": "VIBRATE",
    "Landroid/os/storage/IMountService$Stub$Proxy;-createSecureContainer-(Ljava/lang/String; I Ljava/lang/String; Ljava/lang/String; I)":
    "ASEC_CREATE",
    "Landroid/os/storage/IMountService$Stub$Proxy;-finalizeSecureContainer-(Ljava/lang/String;)":
    "ASEC_CREATE",
    "Landroid/bluetooth/BluetoothAdapter;-setScanMode-(I I)":
    "WRITE_SECURE_SETTINGS",
    "Landroid/bluetooth/BluetoothAdapter;-setScanMode-(I)":
    "WRITE_SECURE_SETTINGS",
    "Landroid/server/BluetoothService;-setScanMode-(I I)":
    "WRITE_SECURE_SETTINGS",
    "Landroid/os/IPowerManager$Stub$Proxy;-setMaximumScreenOffTimeount-(I)":
    "WRITE_SECURE_SETTINGS",
    "Landroid/content/pm/IPackageManager$Stub$Proxy;-setInstallLocation-(I)":
    "WRITE_SECURE_SETTINGS",
    "Landroid/bluetooth/IBluetooth$Stub$Proxy;-setScanMode-(I I)":
    "WRITE_SECURE_SETTINGS",
    "Landroid/view/IWindowManager$Stub$Proxy;-setRotation-(I B I)":
    "SET_ORIENTATION",
    "Lcom/android/internal/app/IUsageStats$Stub$Proxy;-getAllPkgUsageStats-()":
    "PACKAGE_USAGE_STATS",
    "Lcom/android/internal/app/IUsageStats$Stub$Proxy;-getPkgUsageStats-(LComponentName;)":
    "PACKAGE_USAGE_STATS",
    "Landroid/os/IHardwareService$Stub$Proxy;-setFlashlightEnabled-(B)":
    "FLASHLIGHT",
    "Landroid/app/SearchManager;-EXTRA_SELECT_QUERY-Ljava/lang/String;":
    "GLOBAL_SEARCH",
    "Landroid/app/SearchManager;-INTENT_ACTION_GLOBAL_SEARCH-Ljava/lang/String;":
    "GLOBAL_SEARCH",
    "Landroid/server/search/Searchables;-buildSearchableList-()": "GLOBAL_SEARCH",
    "Landroid/server/search/Searchables;-findGlobalSearchActivity-()":
    "GLOBAL_SEARCH",
    "Landroid/net/wifi/IWifiManager$Stub$Proxy;-addOrUpdateNetwork-(Landroid/net/wifi/WifiConfiguration;)":
    "CHANGE_WIFI_STATE",
    "Landroid/net/wifi/IWifiManager$Stub$Proxy;-disableNetwork-(I)":
    "CHANGE_WIFI_STATE",
    "Landroid/net/wifi/IWifiManager$Stub$Proxy;-disconnect-()":
    "CHANGE_WIFI_STATE",
    "Landroid/net/wifi/IWifiManager$Stub$Proxy;-enableNetwork-(I B)":
    "CHANGE_WIFI_STATE",
    "Landroid/net/wifi/IWifiManager$Stub$Proxy;-pingSupplicant-()":
    "CHANGE_WIFI_STATE",
    "Landroid/net/wifi/IWifiManager$Stub$Proxy;-reassociate-()":
    "CHANGE_WIFI_STATE",
    "Landroid/net/wifi/IWifiManager$Stub$Proxy;-reconnect-()":
    "CHANGE_WIFI_STATE",
    "Landroid/net/wifi/IWifiManager$Stub$Proxy;-removeNetwork-(I)":
    "CHANGE_WIFI_STATE",
    "Landroid/net/wifi/IWifiManager$Stub$Proxy;-saveConfiguration-()":
    "CHANGE_WIFI_STATE",
    "Landroid/net/wifi/IWifiManager$Stub$Proxy;-setNumAllowedChannels-(I B)":
    "CHANGE_WIFI_STATE",
    "Landroid/net/wifi/IWifiManager$Stub$Proxy;-setWifiApEnabled-(Landroid/net/wifi/WifiConfiguration; B)":
    "CHANGE_WIFI_STATE",
    "Landroid/net/wifi/IWifiManager$Stub$Proxy;-setWifiEnabled-(B)":
    "CHANGE_WIFI_STATE",
    "Landroid/net/wifi/IWifiManager$Stub$Proxy;-startScan-(B)":
    "CHANGE_WIFI_STATE",
    "Landroid/net/wifi/WifiManager;-addNetwork-(Landroid/net/wifi/WifiConfiguration;)":
    "CHANGE_WIFI_STATE",
    "Landroid/net/wifi/WifiManager;-addOrUpdateNetwork-(Landroid/net/wifi/WifiConfiguration;)":
    "CHANGE_WIFI_STATE",
    "Landroid/net/wifi/WifiManager;-disableNetwork-(I)": "CHANGE_WIFI_STATE",
    "Landroid/net/wifi/WifiManager;-disconnect-()": "CHANGE_WIFI_STATE",
    "Landroid/net/wifi/WifiManager;-enableNetwork-(I B)": "CHANGE_WIFI_STATE",
    "Landroid/net/wifi/WifiManager;-pingSupplicant-()": "CHANGE_WIFI_STATE",
    "Landroid/net/wifi/WifiManager;-reassociate-()": "CHANGE_WIFI_STATE",
    "Landroid/net/wifi/WifiManager;-reconnect-()": "CHANGE_WIFI_STATE",
    "Landroid/net/wifi/WifiManager;-removeNetwork-(I)": "CHANGE_WIFI_STATE",
    "Landroid/net/wifi/WifiManager;-saveConfiguration-()": "CHANGE_WIFI_STATE",
    "Landroid/net/wifi/WifiManager;-setNumAllowedChannels-(I B)":
    "CHANGE_WIFI_STATE",
    "Landroid/net/wifi/WifiManager;-setWifiApEnabled-(Landroid/net/wifi/WifiConfiguration; B)":
    "CHANGE_WIFI_STATE",
    "Landroid/net/wifi/WifiManager;-setWifiEnabled-(B)": "CHANGE_WIFI_STATE",
    "Landroid/net/wifi/WifiManager;-startScan-()": "CHANGE_WIFI_STATE",
    "Landroid/net/wifi/WifiManager;-startScanActive-()": "CHANGE_WIFI_STATE",
    "Landroid/app/ExpandableListActivity;-removeStickyBroadcast-(Landroid/content/Intent;)":
    "BROADCAST_STICKY",
    "Landroid/app/ExpandableListActivity;-sendStickyBroadcast-(Landroid/content/Intent;)":
    "BROADCAST_STICKY",
    "Landroid/app/ExpandableListActivity;-sendStickyOrderedBroadcast-(Landroid/content/Intent; Landroid/content/BroadcastReceiver; Landroid/os/Handler; I Ljava/lang/String; Landroid/os/Bundle;)":
    "BROADCAST_STICKY",
    "Landroid/accessibilityservice/AccessibilityService;-removeStickyBroadcast-(Landroid/content/Intent;)":
    "BROADCAST_STICKY",
    "Landroid/accessibilityservice/AccessibilityService;-sendStickyBroadcast-(Landroid/content/Intent;)":
    "BROADCAST_STICKY",
    "Landroid/accessibilityservice/AccessibilityService;-sendStickyOrderedBroadcast-(Landroid/content/Intent; Landroid/content/BroadcastReceiver; Landroid/os/Handler; I Ljava/lang/String; Landroid/os/Bundle;)":
    "BROADCAST_STICKY",
    "Landroid/accounts/GrantCredentialsPermissionActivity;-removeStickyBroadcast-(Landroid/content/Intent;)":
    "BROADCAST_STICKY",
    "Landroid/accounts/GrantCredentialsPermissionActivity;-sendStickyBroadcast-(Landroid/content/Intent;)":
    "BROADCAST_STICKY",
    "Landroid/accounts/GrantCredentialsPermissionActivity;-sendStickyOrderedBroadcast-(Landroid/content/Intent; Landroid/content/BroadcastReceiver; Landroid/os/Handler; I Ljava/lang/String; Landroid/os/Bundle;)":
    "BROADCAST_STICKY",
    "Landroid/app/backup/BackupAgent;-removeStickyBroadcast-(Landroid/content/Intent;)":
    "BROADCAST_STICKY",
    "Landroid/app/backup/BackupAgent;-sendStickyBroadcast-(Landroid/content/Intent;)":
    "BROADCAST_STICKY",
    "Landroid/app/backup/BackupAgent;-sendStickyOrderedBroadcast-(Landroid/content/Intent; Landroid/content/BroadcastReceiver; Landroid/os/Handler; I Ljava/lang/String; Landroid/os/Bundle;)":
    "BROADCAST_STICKY",
    "Landroid/service/wallpaper/WallpaperService;-removeStickyBroadcast-(Landroid/content/Intent;)":
    "BROADCAST_STICKY",
    "Landroid/service/wallpaper/WallpaperService;-sendStickyBroadcast-(Landroid/content/Intent;)":
    "BROADCAST_STICKY",
    "Landroid/service/wallpaper/WallpaperService;-sendStickyOrderedBroadcast-(Landroid/content/Intent; Landroid/content/BroadcastReceiver; Landroid/os/Handler; I Ljava/lang/String; Landroid/os/Bundle;)":
    "BROADCAST_STICKY",
    "Landroid/app/backup/BackupAgentHelper;-removeStickyBroadcast-(Landroid/content/Intent;)":
    "BROADCAST_STICKY",
    "Landroid/app/backup/BackupAgentHelper;-sendStickyBroadcast-(Landroid/content/Intent;)":
    "BROADCAST_STICKY",
    "Landroid/app/backup/BackupAgentHelper;-sendStickyOrderedBroadcast-(Landroid/content/Intent; Landroid/content/BroadcastReceiver; Landroid/os/Handler; I Ljava/lang/String; Landroid/os/Bundle;)":
    "BROADCAST_STICKY",
    "Landroid/accounts/AccountAuthenticatorActivity;-removeStickyBroadcast-(Landroid/content/Intent;)":
    "BROADCAST_STICKY",
    "Landroid/accounts/AccountAuthenticatorActivity;-sendStickyBroadcast-(Landroid/content/Intent;)":
    "BROADCAST_STICKY",
    "Landroid/accounts/AccountAuthenticatorActivity;-sendStickyOrderedBroadcast-(Landroid/content/Intent; Landroid/content/BroadcastReceiver; Landroid/os/Handler; I Ljava/lang/String; Landroid/os/Bundle;)":
    "BROADCAST_STICKY",
    "Landroid/app/IActivityManager$Stub$Proxy;-unbroadcastIntent-(Landroid/app/IApplicationThread; Landroid/content/Intent;)":
    "BROADCAST_STICKY",
    "Landroid/app/ActivityGroup;-removeStickyBroadcast-(Landroid/content/Intent;)":
    "BROADCAST_STICKY",
    "Landroid/app/ActivityGroup;-sendStickyBroadcast-(Landroid/content/Intent;)":
    "BROADCAST_STICKY",
    "Landroid/app/ActivityGroup;-sendStickyOrderedBroadcast-(Landroid/content/Intent; Landroid/content/BroadcastReceiver; Landroid/os/Handler; I Ljava/lang/String; Landroid/os/Bundle;)":
    "BROADCAST_STICKY",
    "Landroid/content/ContextWrapper;-removeStickyBroadcast-(Landroid/content/Intent;)":
    "BROADCAST_STICKY",
    "Landroid/content/ContextWrapper;-sendStickyBroadcast-(Landroid/content/Intent;)":
    "BROADCAST_STICKY",
    "Landroid/content/ContextWrapper;-removeStickyBroadcast-(Landroid/content/Intent;)":
    "BROADCAST_STICKY",
    "Landroid/content/ContextWrapper;-sendStickyBroadcast-(Landroid/content/Intent;)":
    "BROADCAST_STICKY",
    "Landroid/content/ContextWrapper;-sendStickyOrderedBroadcast-(Landroid/content/Intent; Landroid/content/BroadcastReceiver; Landroid/os/Handler; I Ljava/lang/String; Landroid/os/Bundle;)":
    "BROADCAST_STICKY",
    "Landroid/app/Activity;-removeStickyBroadcast-(Landroid/content/Intent;)":
    "BROADCAST_STICKY",
    "Landroid/app/Activity;-sendStickyBroadcast-(Landroid/content/Intent;)":
    "BROADCAST_STICKY",
    "Landroid/app/Activity;-sendStickyOrderedBroadcast-(Landroid/content/Intent; Landroid/content/BroadcastReceiver; Landroid/os/Handler; I Ljava/lang/String; Landroid/os/Bundle;)":
    "BROADCAST_STICKY",
    "Landroid/app/ContextImpl;-removeStickyBroadcast-(Landroid/content/Intent;)":
    "BROADCAST_STICKY",
    "Landroid/app/ContextImpl;-sendStickyBroadcast-(Landroid/content/Intent;)":
    "BROADCAST_STICKY",
    "Landroid/app/ContextImpl;-sendStickyOrderedBroadcast-(Landroid/content/Intent; Landroid/content/BroadcastReceiver; Landroid/os/Handler; I Ljava/lang/String; Landroid/os/Bundle;)":
    "BROADCAST_STICKY",
    "Landroid/app/AliasActivity;-removeStickyBroadcast-(Landroid/content/Intent;)":
    "BROADCAST_STICKY",
    "Landroid/app/AliasActivity;-sendStickyBroadcast-(Landroid/content/Intent;)":
    "BROADCAST_STICKY",
    "Landroid/app/AliasActivity;-sendStickyOrderedBroadcast-(Landroid/content/Intent; Landroid/content/BroadcastReceiver; Landroid/os/Handler; I Ljava/lang/String; Landroid/os/Bundle;)":
    "BROADCAST_STICKY",
    "Landroid/content/Context;-removeStickyBroadcast-(Landroid/content/Intent;)":
    "BROADCAST_STICKY",
    "Landroid/content/Context;-sendStickyBroadcast-(Landroid/content/Intent;)":
    "BROADCAST_STICKY",
    "Landroid/content/Context;-removeStickyBroadcast-(Landroid/content/Intent;)":
    "BROADCAST_STICKY",
    "Landroid/content/Context;-sendStickyBroadcast-(Landroid/content/Intent;)":
    "BROADCAST_STICKY",
    "Landroid/content/Context;-sendStickyOrderedBroadcast-(Landroid/content/Intent; Landroid/content/BroadcastReceiver; Landroid/os/Handler; I Ljava/lang/String; Landroid/os/Bundle;)":
    "BROADCAST_STICKY",
    "Landroid/service/urlrenderer/UrlRendererService;-removeStickyBroadcast-(Landroid/content/Intent;)":
    "BROADCAST_STICKY",
    "Landroid/service/urlrenderer/UrlRendererService;-sendStickyBroadcast-(Landroid/content/Intent;)":
    "BROADCAST_STICKY",
    "Landroid/service/urlrenderer/UrlRendererService;-sendStickyOrderedBroadcast-(Landroid/content/Intent; Landroid/content/BroadcastReceiver; Landroid/os/Handler; I Ljava/lang/String; Landroid/os/Bundle;)":
    "BROADCAST_STICKY",
    "Landroid/app/FullBackupAgent;-removeStickyBroadcast-(Landroid/content/Intent;)":
    "BROADCAST_STICKY",
    "Landroid/app/FullBackupAgent;-sendStickyBroadcast-(Landroid/content/Intent;)":
    "BROADCAST_STICKY",
    "Landroid/app/FullBackupAgent;-sendStickyOrderedBroadcast-(Landroid/content/Intent; Landroid/content/BroadcastReceiver; Landroid/os/Handler; I Ljava/lang/String; Landroid/os/Bundle;)":
    "BROADCAST_STICKY",
    "Landroid/app/TabActivity;-removeStickyBroadcast-(Landroid/content/Intent;)":
    "BROADCAST_STICKY",
    "Landroid/app/TabActivity;-sendStickyBroadcast-(Landroid/content/Intent;)":
    "BROADCAST_STICKY",
    "Landroid/app/TabActivity;-sendStickyOrderedBroadcast-(Landroid/content/Intent; Landroid/content/BroadcastReceiver; Landroid/os/Handler; I Ljava/lang/String; Landroid/os/Bundle;)":
    "BROADCAST_STICKY",
    "Landroid/view/ContextThemeWrapper;-removeStickyBroadcast-(Landroid/content/Intent;)":
    "BROADCAST_STICKY",
    "Landroid/view/ContextThemeWrapper;-sendStickyBroadcast-(Landroid/content/Intent;)":
    "BROADCAST_STICKY",
    "Landroid/view/ContextThemeWrapper;-sendStickyOrderedBroadcast-(Landroid/content/Intent; Landroid/content/BroadcastReceiver; Landroid/os/Handler; I Ljava/lang/String; Landroid/os/Bundle;)":
    "BROADCAST_STICKY",
    "Landroid/speech/RecognitionService;-removeStickyBroadcast-(Landroid/content/Intent;)":
    "BROADCAST_STICKY",
    "Landroid/speech/RecognitionService;-sendStickyBroadcast-(Landroid/content/Intent;)":
    "BROADCAST_STICKY",
    "Landroid/speech/RecognitionService;-sendStickyOrderedBroadcast-(Landroid/content/Intent; Landroid/content/BroadcastReceiver; Landroid/os/Handler; I Ljava/lang/String; Landroid/os/Bundle;)":
    "BROADCAST_STICKY",
    "Landroid/app/IntentService;-removeStickyBroadcast-(Landroid/content/Intent;)":
    "BROADCAST_STICKY",
    "Landroid/app/IntentService;-sendStickyBroadcast-(Landroid/content/Intent;)":
    "BROADCAST_STICKY",
    "Landroid/app/IntentService;-sendStickyOrderedBroadcast-(Landroid/content/Intent; Landroid/content/BroadcastReceiver; Landroid/os/Handler; I Ljava/lang/String; Landroid/os/Bundle;)":
    "BROADCAST_STICKY",
    "Landroid/inputmethodservice/AbstractInputMethodService;-removeStickyBroadcast-(Landroid/content/Intent;)":
    "BROADCAST_STICKY",
    "Landroid/inputmethodservice/AbstractInputMethodService;-sendStickyBroadcast-(Landroid/content/Intent;)":
    "BROADCAST_STICKY",
    "Landroid/inputmethodservice/AbstractInputMethodService;-sendStickyOrderedBroadcast-(Landroid/content/Intent; Landroid/content/BroadcastReceiver; Landroid/os/Handler; I Ljava/lang/String; Landroid/os/Bundle;)":
    "BROADCAST_STICKY",
    "Landroid/app/Application;-removeStickyBroadcast-(Landroid/content/Intent;)":
    "BROADCAST_STICKY",
    "Landroid/app/Application;-sendStickyBroadcast-(Landroid/content/Intent;)":
    "BROADCAST_STICKY",
    "Landroid/app/Application;-sendStickyOrderedBroadcast-(Landroid/content/Intent; Landroid/content/BroadcastReceiver; Landroid/os/Handler; I Ljava/lang/String; Landroid/os/Bundle;)":
    "BROADCAST_STICKY",
    "Landroid/app/Application;-sendStickyOrderedBroadcast-(Landroid/content/Intent; Landroid/content/BroadcastReceiver; Landroid/os/Handler; I Ljava/lang/String; Landroid/os/Bundle;)":
    "BROADCAST_STICKY",
    "Landroid/app/ListActivity;-removeStickyBroadcast-(Landroid/content/Intent;)":
    "BROADCAST_STICKY",
    "Landroid/app/ListActivity;-sendStickyBroadcast-(Landroid/content/Intent;)":
    "BROADCAST_STICKY",
    "Landroid/app/ListActivity;-sendStickyOrderedBroadcast-(Landroid/content/Intent; Landroid/content/BroadcastReceiver; Landroid/os/Handler; I Ljava/lang/String; Landroid/os/Bundle;)":
    "BROADCAST_STICKY",
    "Landroid/app/Service;-removeStickyBroadcast-(Landroid/content/Intent;)":
    "BROADCAST_STICKY",
    "Landroid/app/Service;-sendStickyBroadcast-(Landroid/content/Intent;)":
    "BROADCAST_STICKY",
    "Landroid/app/Service;-sendStickyOrderedBroadcast-(Landroid/content/Intent; Landroid/content/BroadcastReceiver; Landroid/os/Handler; I Ljava/lang/String; Landroid/os/Bundle;)":
    "BROADCAST_STICKY",
    "Landroid/content/MutableContextWrapper;-removeStickyBroadcast-(Landroid/content/Intent;)":
    "BROADCAST_STICKY",
    "Landroid/content/MutableContextWrapper;-sendStickyBroadcast-(Landroid/content/Intent;)":
    "BROADCAST_STICKY",
    "Landroid/content/MutableContextWrapper;-sendStickyOrderedBroadcast-(Landroid/content/Intent; Landroid/content/BroadcastReceiver; Landroid/os/Handler; I Ljava/lang/String; Landroid/os/Bundle;)":
    "BROADCAST_STICKY",
    "Landroid/app/IActivityManager$Stub$Proxy;-forceStopPackage-(Ljava/lang/String;)":
    "FORCE_STOP_PACKAGES",
    "Landroid/app/ActivityManagerNative;-forceStopPackage-(Ljava/lang/String;)":
    "FORCE_STOP_PACKAGES",
    "Landroid/app/ActivityManager;-forceStopPackage-(Ljava/lang/String;)":
    "FORCE_STOP_PACKAGES",
    "Landroid/app/IActivityManager$Stub$Proxy;-killBackgroundProcesses-(Ljava/lang/String;)":
    "KILL_BACKGROUND_PROCESSES",
    "Landroid/app/ActivityManager;-killBackgroundProcesses-(Ljava/lang/String;)":
    "KILL_BACKGROUND_PROCESSES",
    "Landroid/app/AlarmManager;-setTimeZone-(Ljava/lang/String;)": "SET_TIME_ZONE",
    "Landroid/app/AlarmManager;-setTimeZone-(Ljava/lang/String;)": "SET_TIME_ZONE",
    "Landroid/app/IAlarmManager$Stub$Proxy;-setTimeZone-(Ljava/lang/String;)":
    "SET_TIME_ZONE",
    "Landroid/server/BluetoothA2dpService;-connectSink-(Landroid/bluetooth/BluetoothDevice;)":
    "BLUETOOTH_ADMIN",
    "Landroid/server/BluetoothA2dpService;-disconnectSink-(Landroid/bluetooth/BluetoothDevice;)":
    "BLUETOOTH_ADMIN",
    "Landroid/server/BluetoothA2dpService;-resumeSink-(Landroid/bluetooth/BluetoothDevice;)":
    "BLUETOOTH_ADMIN",
    "Landroid/server/BluetoothA2dpService;-setSinkPriority-(Landroid/bluetooth/BluetoothDevice; I)":
    "BLUETOOTH_ADMIN",
    "Landroid/server/BluetoothA2dpService;-setSinkPriority-(Landroid/bluetooth/BluetoothDevice; I)":
    "BLUETOOTH_ADMIN",
    "Landroid/server/BluetoothA2dpService;-suspendSink-(Landroid/bluetooth/BluetoothDevice;)":
    "BLUETOOTH_ADMIN",
    "Landroid/bluetooth/BluetoothPbap;-disconnect-()": "BLUETOOTH_ADMIN",
    "Landroid/bluetooth/IBluetoothA2dp$Stub$Proxy;-connectSink-(Landroid/bluetooth/BluetoothDevice;)":
    "BLUETOOTH_ADMIN",
    "Landroid/bluetooth/IBluetoothA2dp$Stub$Proxy;-disconnectSink-(Landroid/bluetooth/BluetoothDevice;)":
    "BLUETOOTH_ADMIN",
    "Landroid/bluetooth/IBluetoothA2dp$Stub$Proxy;-resumeSink-(Landroid/bluetooth/BluetoothDevice;)":
    "BLUETOOTH_ADMIN",
    "Landroid/bluetooth/IBluetoothA2dp$Stub$Proxy;-setSinkPriority-(Landroid/bluetooth/BluetoothDevice; I)":
    "BLUETOOTH_ADMIN",
    "Landroid/bluetooth/IBluetoothA2dp$Stub$Proxy;-suspendSink-(Landroid/bluetooth/BluetoothDevice;)":
    "BLUETOOTH_ADMIN",
    "Landroid/bluetooth/BluetoothAdapter;-cancelDiscovery-()": "BLUETOOTH_ADMIN",
    "Landroid/bluetooth/BluetoothAdapter;-disable-()": "BLUETOOTH_ADMIN",
    "Landroid/bluetooth/BluetoothAdapter;-enable-()": "BLUETOOTH_ADMIN",
    "Landroid/bluetooth/BluetoothAdapter;-setName-(Ljava/lang/String;)":
    "BLUETOOTH_ADMIN",
    "Landroid/bluetooth/BluetoothAdapter;-startDiscovery-()": "BLUETOOTH_ADMIN",
    "Landroid/bluetooth/BluetoothAdapter;-cancelDiscovery-()": "BLUETOOTH_ADMIN",
    "Landroid/bluetooth/BluetoothAdapter;-disable-()": "BLUETOOTH_ADMIN",
    "Landroid/bluetooth/BluetoothAdapter;-enable-()": "BLUETOOTH_ADMIN",
    "Landroid/bluetooth/BluetoothAdapter;-setDiscoverableTimeout-(I)":
    "BLUETOOTH_ADMIN",
    "Landroid/bluetooth/BluetoothAdapter;-setName-(Ljava/lang/String;)":
    "BLUETOOTH_ADMIN",
    "Landroid/bluetooth/BluetoothAdapter;-startDiscovery-()": "BLUETOOTH_ADMIN",
    "Landroid/server/BluetoothService;-cancelBondProcess-(Ljava/lang/String;)":
    "BLUETOOTH_ADMIN",
    "Landroid/server/BluetoothService;-cancelDiscovery-()": "BLUETOOTH_ADMIN",
    "Landroid/server/BluetoothService;-cancelPairingUserInput-(Ljava/lang/String;)":
    "BLUETOOTH_ADMIN",
    "Landroid/server/BluetoothService;-createBond-(Ljava/lang/String;)":
    "BLUETOOTH_ADMIN",
    "Landroid/server/BluetoothService;-disable-()": "BLUETOOTH_ADMIN",
    "Landroid/server/BluetoothService;-disable-(B)": "BLUETOOTH_ADMIN",
    "Landroid/server/BluetoothService;-enable-()": "BLUETOOTH_ADMIN",
    "Landroid/server/BluetoothService;-enable-(B)": "BLUETOOTH_ADMIN",
    "Landroid/server/BluetoothService;-removeBond-(Ljava/lang/String;)":
    "BLUETOOTH_ADMIN",
    "Landroid/server/BluetoothService;-setDiscoverableTimeout-(I)":
    "BLUETOOTH_ADMIN",
    "Landroid/server/BluetoothService;-setName-(Ljava/lang/String;)":
    "BLUETOOTH_ADMIN",
    "Landroid/server/BluetoothService;-setPairingConfirmation-(Ljava/lang/String; B)":
    "BLUETOOTH_ADMIN",
    "Landroid/server/BluetoothService;-setPasskey-(Ljava/lang/String; I)":
    "BLUETOOTH_ADMIN",
    "Landroid/server/BluetoothService;-setPin-(Ljava/lang/String; [L;)":
    "BLUETOOTH_ADMIN",
    "Landroid/server/BluetoothService;-setTrust-(Ljava/lang/String; B)":
    "BLUETOOTH_ADMIN",
    "Landroid/server/BluetoothService;-startDiscovery-()": "BLUETOOTH_ADMIN",
    "Landroid/bluetooth/BluetoothHeadset;-connectHeadset-(Landroid/bluetooth/BluetoothDevice;)":
    "BLUETOOTH_ADMIN",
    "Landroid/bluetooth/BluetoothHeadset;-disconnectHeadset-()": "BLUETOOTH_ADMIN",
    "Landroid/bluetooth/BluetoothHeadset;-setPriority-(Landroid/bluetooth/BluetoothDevice; I)":
    "BLUETOOTH_ADMIN",
    "Landroid/bluetooth/IBluetoothHeadset$Stub$Proxy;-connectHeadset-(Landroid/bluetooth/BluetoothDevice;)":
    "BLUETOOTH_ADMIN",
    "Landroid/bluetooth/IBluetoothHeadset$Stub$Proxy;-disconnectHeadset-()":
    "BLUETOOTH_ADMIN",
    "Landroid/bluetooth/IBluetoothHeadset$Stub$Proxy;-setPriority-(Landroid/bluetooth/BluetoothDevice; I)":
    "BLUETOOTH_ADMIN",
    "Landroid/bluetooth/BluetoothDevice;-cancelBondProcess-()": "BLUETOOTH_ADMIN",
    "Landroid/bluetooth/BluetoothDevice;-cancelPairingUserInput-()":
    "BLUETOOTH_ADMIN",
    "Landroid/bluetooth/BluetoothDevice;-createBond-()": "BLUETOOTH_ADMIN",
    "Landroid/bluetooth/BluetoothDevice;-removeBond-()": "BLUETOOTH_ADMIN",
    "Landroid/bluetooth/BluetoothDevice;-setPairingConfirmation-(B)":
    "BLUETOOTH_ADMIN",
    "Landroid/bluetooth/BluetoothDevice;-setPasskey-(I)": "BLUETOOTH_ADMIN",
    "Landroid/bluetooth/BluetoothDevice;-setPin-([L;)": "BLUETOOTH_ADMIN",
    "Landroid/bluetooth/IBluetoothPbap$Stub$Proxy;-connect-(Landroid/bluetooth/BluetoothDevice;)":
    "BLUETOOTH_ADMIN",
    "Landroid/bluetooth/IBluetoothPbap$Stub$Proxy;-disconnect-()":
    "BLUETOOTH_ADMIN",
    "Landroid/bluetooth/BluetoothA2dp;-connectSink-(Landroid/bluetooth/BluetoothDevice;)":
    "BLUETOOTH_ADMIN",
    "Landroid/bluetooth/BluetoothA2dp;-disconnectSink-(Landroid/bluetooth/BluetoothDevice;)":
    "BLUETOOTH_ADMIN",
    "Landroid/bluetooth/BluetoothA2dp;-resumeSink-(Landroid/bluetooth/BluetoothDevice;)":
    "BLUETOOTH_ADMIN",
    "Landroid/bluetooth/BluetoothA2dp;-setSinkPriority-(Landroid/bluetooth/BluetoothDevice; I)":
    "BLUETOOTH_ADMIN",
    "Landroid/bluetooth/BluetoothA2dp;-suspendSink-(Landroid/bluetooth/BluetoothDevice;)":
    "BLUETOOTH_ADMIN",
    "Landroid/bluetooth/IBluetooth$Stub$Proxy;-cancelBondProcess-(Ljava/lang/String;)":
    "BLUETOOTH_ADMIN",
    "Landroid/bluetooth/IBluetooth$Stub$Proxy;-cancelDiscovery-()":
    "BLUETOOTH_ADMIN",
    "Landroid/bluetooth/IBluetooth$Stub$Proxy;-cancelPairingUserInput-(Ljava/lang/String;)":
    "BLUETOOTH_ADMIN",
    "Landroid/bluetooth/IBluetooth$Stub$Proxy;-createBond-(Ljava/lang/String;)":
    "BLUETOOTH_ADMIN",
    "Landroid/bluetooth/IBluetooth$Stub$Proxy;-disable-(B)": "BLUETOOTH_ADMIN",
    "Landroid/bluetooth/IBluetooth$Stub$Proxy;-enable-()": "BLUETOOTH_ADMIN",
    "Landroid/bluetooth/IBluetooth$Stub$Proxy;-removeBond-(Ljava/lang/String;)":
    "BLUETOOTH_ADMIN",
    "Landroid/bluetooth/IBluetooth$Stub$Proxy;-setDiscoverableTimeout-(I)":
    "BLUETOOTH_ADMIN",
    "Landroid/bluetooth/IBluetooth$Stub$Proxy;-setName-(Ljava/lang/String;)":
    "BLUETOOTH_ADMIN",
    "Landroid/bluetooth/IBluetooth$Stub$Proxy;-setPairingConfirmation-(Ljava/lang/String; B)":
    "BLUETOOTH_ADMIN",
    "Landroid/bluetooth/IBluetooth$Stub$Proxy;-setPasskey-(Ljava/lang/String; I)":
    "BLUETOOTH_ADMIN",
    "Landroid/bluetooth/IBluetooth$Stub$Proxy;-setPin-(Ljava/lang/String; [L;)":
    "BLUETOOTH_ADMIN",
    "Landroid/bluetooth/IBluetooth$Stub$Proxy;-setTrust-(Ljava/lang/String; B)":
    "BLUETOOTH_ADMIN",
    "Landroid/bluetooth/IBluetooth$Stub$Proxy;-startDiscovery-()":
    "BLUETOOTH_ADMIN",
    "Landroid/view/IWindowManager$Stub$Proxy;-injectKeyEvent-(Landroid/view/KeyEvent; B)":
    "INJECT_EVENTS",
    "Landroid/view/IWindowManager$Stub$Proxy;-injectPointerEvent-(Landroid/view/MotionEvent; B)":
    "INJECT_EVENTS",
    "Landroid/view/IWindowManager$Stub$Proxy;-injectTrackballEvent-(Landroid/view/MotionEvent; B)":
    "INJECT_EVENTS",
    "Landroid/app/Instrumentation;-invokeContextMenuAction-(Landroid/app/Activity; I I)":
    "INJECT_EVENTS",
    "Landroid/app/Instrumentation;-sendCharacterSync-(I)": "INJECT_EVENTS",
    "Landroid/app/Instrumentation;-sendKeyDownUpSync-(I)": "INJECT_EVENTS",
    "Landroid/app/Instrumentation;-sendKeySync-(Landroid/view/KeyEvent;)":
    "INJECT_EVENTS",
    "Landroid/app/Instrumentation;-sendPointerSync-(Landroid/view/MotionEvent;)":
    "INJECT_EVENTS",
    "Landroid/app/Instrumentation;-sendStringSync-(Ljava/lang/String;)":
    "INJECT_EVENTS",
    "Landroid/app/Instrumentation;-sendTrackballEventSync-(Landroid/view/MotionEvent;)":
    "INJECT_EVENTS",
    "Landroid/hardware/Camera/ErrorCallback;-onError-(I Landroid/hardware/Camera;)":
    "CAMERA",
    "Landroid/media/MediaRecorder;-setVideoSource-(I)": "CAMERA",
    "Landroid/view/KeyEvent;-KEYCODE_CAMERA-I": "CAMERA",
    "Landroid/bluetooth/BluetoothClass/Device;-AUDIO_VIDEO_VIDEO_CAMERA-I":
    "CAMERA",
    "Landroid/provider/MediaStore;-INTENT_ACTION_STILL_IMAGE_CAMERA-Ljava/lang/String;":
    "CAMERA",
    "Landroid/provider/MediaStore;-INTENT_ACTION_VIDEO_CAMERA-Ljava/lang/String;":
    "CAMERA",
    "Landroid/hardware/Camera/CameraInfo;-CAMERA_FACING_BACK-I": "CAMERA",
    "Landroid/hardware/Camera/CameraInfo;-CAMERA_FACING_FRONT-I": "CAMERA",
    "Landroid/hardware/Camera/CameraInfo;-facing-I": "CAMERA",
    "Landroid/provider/ContactsContract/StatusColumns;-CAPABILITY_HAS_CAMERA-I":
    "CAMERA",
    "Landroid/hardware/Camera/Parameters;-setRotation-(I)": "CAMERA",
    "Landroid/media/MediaRecorder/VideoSource;-CAMERA-I": "CAMERA",
    "Landroid/content/Intent;-IntentResolution-Ljava/lang/String;": "CAMERA",
    "Landroid/content/Intent;-ACTION_CAMERA_BUTTON-Ljava/lang/String;": "CAMERA",
    "Landroid/content/pm/PackageManager;-FEATURE_CAMERA-Ljava/lang/String;":
    "CAMERA",
    "Landroid/content/pm/PackageManager;-FEATURE_CAMERA_AUTOFOCUS-Ljava/lang/String;":
    "CAMERA",
    "Landroid/content/pm/PackageManager;-FEATURE_CAMERA_FLASH-Ljava/lang/String;":
    "CAMERA",
    "Landroid/content/pm/PackageManager;-FEATURE_CAMERA_FRONT-Ljava/lang/String;":
    "CAMERA",
    "Landroid/hardware/Camera;-CAMERA_ERROR_SERVER_DIED-I": "CAMERA",
    "Landroid/hardware/Camera;-CAMERA_ERROR_UNKNOWN-I": "CAMERA",
    "Landroid/hardware/Camera;-setDisplayOrientation-(I)": "CAMERA",
    "Landroid/hardware/Camera;-native_setup-(Ljava/lang/Object;)": "CAMERA",
    "Landroid/hardware/Camera;-open-()": "CAMERA",
    "Landroid/app/Activity;-clearWallpaper-()": "SET_WALLPAPER",
    "Landroid/app/Activity;-setWallpaper-(Landroid/graphics/Bitmap;)":
    "SET_WALLPAPER",
    "Landroid/app/Activity;-setWallpaper-(Ljava/io/InputStream;)": "SET_WALLPAPER",
    "Landroid/app/ExpandableListActivity;-clearWallpaper-()": "SET_WALLPAPER",
    "Landroid/app/ExpandableListActivity;-setWallpaper-(Landroid/graphics/Bitmap;)":
    "SET_WALLPAPER",
    "Landroid/app/ExpandableListActivity;-setWallpaper-(Ljava/io/InputStream;)":
    "SET_WALLPAPER",
    "Landroid/accessibilityservice/AccessibilityService;-clearWallpaper-()":
    "SET_WALLPAPER",
    "Landroid/accessibilityservice/AccessibilityService;-setWallpaper-(Landroid/graphics/Bitmap;)":
    "SET_WALLPAPER",
    "Landroid/accessibilityservice/AccessibilityService;-setWallpaper-(Ljava/io/InputStream;)":
    "SET_WALLPAPER",
    "Landroid/accounts/GrantCredentialsPermissionActivity;-clearWallpaper-()":
    "SET_WALLPAPER",
    "Landroid/accounts/GrantCredentialsPermissionActivity;-setWallpaper-(Landroid/graphics/Bitmap;)":
    "SET_WALLPAPER",
    "Landroid/accounts/GrantCredentialsPermissionActivity;-setWallpaper-(Ljava/io/InputStream;)":
    "SET_WALLPAPER",
    "Landroid/app/backup/BackupAgent;-clearWallpaper-()": "SET_WALLPAPER",
    "Landroid/app/backup/BackupAgent;-setWallpaper-(Landroid/graphics/Bitmap;)":
    "SET_WALLPAPER",
    "Landroid/app/backup/BackupAgent;-setWallpaper-(Ljava/io/InputStream;)":
    "SET_WALLPAPER",
    "Landroid/service/wallpaper/WallpaperService;-clearWallpaper-()":
    "SET_WALLPAPER",
    "Landroid/service/wallpaper/WallpaperService;-setWallpaper-(Landroid/graphics/Bitmap;)":
    "SET_WALLPAPER",
    "Landroid/service/wallpaper/WallpaperService;-setWallpaper-(Ljava/io/InputStream;)":
    "SET_WALLPAPER",
    "Landroid/app/backup/BackupAgentHelper;-clearWallpaper-()": "SET_WALLPAPER",
    "Landroid/app/backup/BackupAgentHelper;-setWallpaper-(Landroid/graphics/Bitmap;)":
    "SET_WALLPAPER",
    "Landroid/app/backup/BackupAgentHelper;-setWallpaper-(Ljava/io/InputStream;)":
    "SET_WALLPAPER",
    "Landroid/accounts/AccountAuthenticatorActivity;-clearWallpaper-()":
    "SET_WALLPAPER",
    "Landroid/accounts/AccountAuthenticatorActivity;-setWallpaper-(Landroid/graphics/Bitmap;)":
    "SET_WALLPAPER",
    "Landroid/accounts/AccountAuthenticatorActivity;-setWallpaper-(Ljava/io/InputStream;)":
    "SET_WALLPAPER",
    "Landroid/app/IWallpaperManager$Stub$Proxy;-setWallpaper-(Ljava/lang/String;)":
    "SET_WALLPAPER",
    "Landroid/app/ActivityGroup;-clearWallpaper-()": "SET_WALLPAPER",
    "Landroid/app/ActivityGroup;-setWallpaper-(Landroid/graphics/Bitmap;)":
    "SET_WALLPAPER",
    "Landroid/app/ActivityGroup;-setWallpaper-(Ljava/io/InputStream;)":
    "SET_WALLPAPER",
    "Landroid/content/ContextWrapper;-clearWallpaper-()": "SET_WALLPAPER",
    "Landroid/content/ContextWrapper;-setWallpaper-(Landroid/graphics/Bitmap;)":
    "SET_WALLPAPER",
    "Landroid/content/ContextWrapper;-setWallpaper-(Ljava/io/InputStream;)":
    "SET_WALLPAPER",
    "Landroid/app/WallpaperManager;-setBitmap-(Landroid/graphics/Bitmap;)":
    "SET_WALLPAPER",
    "Landroid/app/WallpaperManager;-clear-()": "SET_WALLPAPER",
    "Landroid/app/WallpaperManager;-setBitmap-(Landroid/graphics/Bitmap;)":
    "SET_WALLPAPER",
    "Landroid/app/WallpaperManager;-setResource-(I)": "SET_WALLPAPER",
    "Landroid/app/WallpaperManager;-setStream-(Ljava/io/InputStream;)":
    "SET_WALLPAPER",
    "Landroid/app/ContextImpl;-clearWallpaper-()": "SET_WALLPAPER",
    "Landroid/app/ContextImpl;-setWallpaper-(Landroid/graphics/Bitmap;)":
    "SET_WALLPAPER",
    "Landroid/app/ContextImpl;-setWallpaper-(Ljava/io/InputStream;)":
    "SET_WALLPAPER",
    "Landroid/app/AliasActivity;-clearWallpaper-()": "SET_WALLPAPER",
    "Landroid/app/AliasActivity;-setWallpaper-(Landroid/graphics/Bitmap;)":
    "SET_WALLPAPER",
    "Landroid/app/AliasActivity;-setWallpaper-(Ljava/io/InputStream;)":
    "SET_WALLPAPER",
    "Landroid/content/Context;-clearWallpaper-()": "SET_WALLPAPER",
    "Landroid/content/Context;-setWallpaper-(Landroid/graphics/Bitmap;)":
    "SET_WALLPAPER",
    "Landroid/content/Context;-setWallpaper-(Ljava/io/InputStream;)":
    "SET_WALLPAPER",
    "Landroid/service/urlrenderer/UrlRendererService;-clearWallpaper-()":
    "SET_WALLPAPER",
    "Landroid/service/urlrenderer/UrlRendererService;-setWallpaper-(Landroid/graphics/Bitmap;)":
    "SET_WALLPAPER",
    "Landroid/service/urlrenderer/UrlRendererService;-setWallpaper-(Ljava/io/InputStream;)":
    "SET_WALLPAPER",
    "Landroid/app/FullBackupAgent;-clearWallpaper-()": "SET_WALLPAPER",
    "Landroid/app/FullBackupAgent;-setWallpaper-(Landroid/graphics/Bitmap;)":
    "SET_WALLPAPER",
    "Landroid/app/FullBackupAgent;-setWallpaper-(Ljava/io/InputStream;)":
    "SET_WALLPAPER",
    "Landroid/app/TabActivity;-clearWallpaper-()": "SET_WALLPAPER",
    "Landroid/app/TabActivity;-setWallpaper-(Landroid/graphics/Bitmap;)":
    "SET_WALLPAPER",
    "Landroid/app/TabActivity;-setWallpaper-(Ljava/io/InputStream;)":
    "SET_WALLPAPER",
    "Landroid/view/ContextThemeWrapper;-clearWallpaper-()": "SET_WALLPAPER",
    "Landroid/view/ContextThemeWrapper;-setWallpaper-(Landroid/graphics/Bitmap;)":
    "SET_WALLPAPER",
    "Landroid/view/ContextThemeWrapper;-setWallpaper-(Ljava/io/InputStream;)":
    "SET_WALLPAPER",
    "Landroid/speech/RecognitionService;-clearWallpaper-()": "SET_WALLPAPER",
    "Landroid/speech/RecognitionService;-setWallpaper-(Landroid/graphics/Bitmap;)":
    "SET_WALLPAPER",
    "Landroid/speech/RecognitionService;-setWallpaper-(Ljava/io/InputStream;)":
    "SET_WALLPAPER",
    "Landroid/app/IntentService;-clearWallpaper-()": "SET_WALLPAPER",
    "Landroid/app/IntentService;-setWallpaper-(Landroid/graphics/Bitmap;)":
    "SET_WALLPAPER",
    "Landroid/app/IntentService;-setWallpaper-(Ljava/io/InputStream;)":
    "SET_WALLPAPER",
    "Landroid/inputmethodservice/AbstractInputMethodService;-clearWallpaper-()":
    "SET_WALLPAPER",
    "Landroid/inputmethodservice/AbstractInputMethodService;-setWallpaper-(Landroid/graphics/Bitmap;)":
    "SET_WALLPAPER",
    "Landroid/inputmethodservice/AbstractInputMethodService;-setWallpaper-(Ljava/io/InputStream;)":
    "SET_WALLPAPER",
    "Landroid/app/Application;-clearWallpaper-()": "SET_WALLPAPER",
    "Landroid/app/Application;-setWallpaper-(Landroid/graphics/Bitmap;)":
    "SET_WALLPAPER",
    "Landroid/app/Application;-setWallpaper-(Ljava/io/InputStream;)":
    "SET_WALLPAPER",
    "Landroid/app/ListActivity;-clearWallpaper-()": "SET_WALLPAPER",
    "Landroid/app/ListActivity;-setWallpaper-(Landroid/graphics/Bitmap;)":
    "SET_WALLPAPER",
    "Landroid/app/ListActivity;-setWallpaper-(Ljava/io/InputStream;)":
    "SET_WALLPAPER",
    "Landroid/app/Service;-clearWallpaper-()": "SET_WALLPAPER",
    "Landroid/app/Service;-setWallpaper-(Landroid/graphics/Bitmap;)":
    "SET_WALLPAPER",
    "Landroid/app/Service;-setWallpaper-(Ljava/io/InputStream;)": "SET_WALLPAPER",
    "Landroid/content/MutableContextWrapper;-clearWallpaper-()": "SET_WALLPAPER",
    "Landroid/content/MutableContextWrapper;-setWallpaper-(Landroid/graphics/Bitmap;)":
    "SET_WALLPAPER",
    "Landroid/content/MutableContextWrapper;-setWallpaper-(Ljava/io/InputStream;)":
    "SET_WALLPAPER",
    "Landroid/net/wifi/IWifiManager$Stub$Proxy;-acquireWifiLock-(Landroid/os/IBinder; I Ljava/lang/String;)":
    "WAKE_LOCK",
    "Landroid/net/wifi/IWifiManager$Stub$Proxy;-releaseWifiLock-(Landroid/os/IBinder;)":
    "WAKE_LOCK",
    "Landroid/bluetooth/HeadsetBase;-acquireWakeLock-()": "WAKE_LOCK",
    "Landroid/bluetooth/HeadsetBase;-finalize-()": "WAKE_LOCK",
    "Landroid/bluetooth/HeadsetBase;-handleInput-(Ljava/lang/String;)": "WAKE_LOCK",
    "Landroid/bluetooth/HeadsetBase;-releaseWakeLock-()": "WAKE_LOCK",
    "Landroid/os/PowerManager$WakeLock;-acquire-()": "WAKE_LOCK",
    "Landroid/os/PowerManager$WakeLock;-acquire-(J)": "WAKE_LOCK",
    "Landroid/os/PowerManager$WakeLock;-release-()": "WAKE_LOCK",
    "Landroid/os/PowerManager$WakeLock;-release-(I)": "WAKE_LOCK",
    "Landroid/media/MediaPlayer;-setWakeMode-(Landroid/content/Context; I)":
    "WAKE_LOCK",
    "Landroid/media/MediaPlayer;-start-()": "WAKE_LOCK",
    "Landroid/media/MediaPlayer;-stayAwake-(B)": "WAKE_LOCK",
    "Landroid/media/MediaPlayer;-stop-()": "WAKE_LOCK",
    "Landroid/bluetooth/ScoSocket;-acquireWakeLock-()": "WAKE_LOCK",
    "Landroid/bluetooth/ScoSocket;-close-()": "WAKE_LOCK",
    "Landroid/bluetooth/ScoSocket;-finalize-()": "WAKE_LOCK",
    "Landroid/bluetooth/ScoSocket;-releaseWakeLock-()": "WAKE_LOCK",
    "Landroid/bluetooth/ScoSocket;-releaseWakeLockNow-()": "WAKE_LOCK",
    "Landroid/media/AsyncPlayer;-acquireWakeLock-()": "WAKE_LOCK",
    "Landroid/media/AsyncPlayer;-enqueueLocked-(Landroid/media/AsyncPlayer$Command;)":
    "WAKE_LOCK",
    "Landroid/media/AsyncPlayer;-play-(Landroid/content/Context; Landroid/net/Uri; B I)":
    "WAKE_LOCK",
    "Landroid/media/AsyncPlayer;-releaseWakeLock-()": "WAKE_LOCK",
    "Landroid/media/AsyncPlayer;-stop-()": "WAKE_LOCK",
    "Landroid/net/wifi/WifiManager$WifiLock;-acquire-()": "WAKE_LOCK",
    "Landroid/net/wifi/WifiManager$WifiLock;-finalize-()": "WAKE_LOCK",
    "Landroid/net/wifi/WifiManager$WifiLock;-release-()": "WAKE_LOCK",
    "Landroid/os/IPowerManager$Stub$Proxy;-acquireWakeLock-(I Landroid/os/IBinder; Ljava/lang/String;)":
    "WAKE_LOCK",
    "Landroid/os/IPowerManager$Stub$Proxy;-releaseWakeLock-(Landroid/os/IBinder; I)":
    "WAKE_LOCK",
    "Landroid/net/sip/SipAudioCall;-startAudio-()": "WAKE_LOCK",
    "Landroid/os/PowerManager;-ACQUIRE_CAUSES_WAKEUP-I": "WAKE_LOCK",
    "Landroid/os/PowerManager;-FULL_WAKE_LOCK-I": "WAKE_LOCK",
    "Landroid/os/PowerManager;-ON_AFTER_RELEASE-I": "WAKE_LOCK",
    "Landroid/os/PowerManager;-PARTIAL_WAKE_LOCK-I": "WAKE_LOCK",
    "Landroid/os/PowerManager;-SCREEN_BRIGHT_WAKE_LOCK-I": "WAKE_LOCK",
    "Landroid/os/PowerManager;-SCREEN_DIM_WAKE_LOCK-I": "WAKE_LOCK",
    "Landroid/os/PowerManager;-newWakeLock-(I Ljava/lang/String;)": "WAKE_LOCK",
    "Landroid/accounts/AccountManager;-addAccount-(Ljava/lang/String; Ljava/lang/String; [Ljava/lang/String; Landroid/os/Bundle; Landroid/app/Activity; Landroid/accounts/AccountManagerCallback<android/os/Bundle>; Landroid/os/Handler;)":
    "MANAGE_ACCOUNTS",
    "Landroid/accounts/AccountManager;-clearPassword-(Landroid/accounts/Account;)":
    "MANAGE_ACCOUNTS",
    "Landroid/accounts/AccountManager;-confirmCredentials-(Landroid/accounts/Account; Landroid/os/Bundle; Landroid/app/Activity; Landroid/accounts/AccountManagerCallback<android/os/Bundle>; Landroid/os/Handler;)":
    "MANAGE_ACCOUNTS",
    "Landroid/accounts/AccountManager;-editProperties-(Ljava/lang/String; Landroid/app/Activity; Landroid/accounts/AccountManagerCallback<android/os/Bundle>; Landroid/os/Handler;)":
    "MANAGE_ACCOUNTS",
    "Landroid/accounts/AccountManager;-getAuthTokenByFeatures-(Ljava/lang/String; Ljava/lang/String; [Ljava/lang/String; Landroid/app/Activity; Landroid/os/Bundle; Landroid/os/Bundle; Landroid/accounts/AccountManagerCallback<android/os/Bundle>; Landroid/os/Handler;)":
    "MANAGE_ACCOUNTS",
    "Landroid/accounts/AccountManager;-invalidateAuthToken-(Ljava/lang/String; Ljava/lang/String;)":
    "MANAGE_ACCOUNTS",
    "Landroid/accounts/AccountManager;-removeAccount-(Landroid/accounts/Account; Landroid/accounts/AccountManagerCallback<java/lang/Boolean>; Landroid/os/Handler;)":
    "MANAGE_ACCOUNTS",
    "Landroid/accounts/AccountManager;-updateCredentials-(Landroid/accounts/Account; Ljava/lang/String; Landroid/os/Bundle; Landroid/app/Activity; Landroid/accounts/AccountManagerCallback<android/os/Bundle>; Landroid/os/Handler;)":
    "MANAGE_ACCOUNTS",
    "Landroid/accounts/AccountManager;-addAccount-(Ljava/lang/String; Ljava/lang/String; [L[Ljava/lang/Strin; Landroid/os/Bundle; Landroid/app/Activity; Landroid/accounts/AccountManagerCallback; Landroid/os/Handler;)":
    "MANAGE_ACCOUNTS",
    "Landroid/accounts/AccountManager;-clearPassword-(Landroid/accounts/Account;)":
    "MANAGE_ACCOUNTS",
    "Landroid/accounts/AccountManager;-confirmCredentials-(Landroid/accounts/Account; Landroid/os/Bundle; Landroid/app/Activity; Landroid/accounts/AccountManagerCallback; Landroid/os/Handler;)":
    "MANAGE_ACCOUNTS",
    "Landroid/accounts/AccountManager;-editProperties-(Ljava/lang/String; Landroid/app/Activity; Landroid/accounts/AccountManagerCallback; Landroid/os/Handler;)":
    "MANAGE_ACCOUNTS",
    "Landroid/accounts/AccountManager;-invalidateAuthToken-(Ljava/lang/String; Ljava/lang/String;)":
    "MANAGE_ACCOUNTS",
    "Landroid/accounts/AccountManager;-removeAccount-(Landroid/accounts/Account; Landroid/accounts/AccountManagerCallback; Landroid/os/Handler;)":
    "MANAGE_ACCOUNTS",
    "Landroid/accounts/AccountManager;-updateCredentials-(Landroid/accounts/Account; Ljava/lang/String; Landroid/os/Bundle; Landroid/app/Activity; Landroid/accounts/AccountManagerCallback; Landroid/os/Handler;)":
    "MANAGE_ACCOUNTS",
    "Landroid/accounts/AccountManagerService;-addAcount-(Landroid/accounts/IAccountManagerResponse; Ljava/lang/String; Ljava/lang/String; [L[Ljava/lang/Strin; B Landroid/os/Bundle;)":
    "MANAGE_ACCOUNTS",
    "Landroid/accounts/AccountManagerService;-checkManageAccountsOrUseCredentialsPermissions-()":
    "MANAGE_ACCOUNTS",
    "Landroid/accounts/AccountManagerService;-checkManageAccountsPermission-()":
    "MANAGE_ACCOUNTS",
    "Landroid/accounts/AccountManagerService;-clearPassword-(Landroid/accounts/Account;)":
    "MANAGE_ACCOUNTS",
    "Landroid/accounts/AccountManagerService;-confirmCredentials-(Landroid/accounts/IAccountManagerResponse; Landroid/accounts/Account; Landroid/os/Bundle; B)":
    "MANAGE_ACCOUNTS",
    "Landroid/accounts/AccountManagerService;-editProperties-(Landroid/accounts/IAccountManagerResponse; Ljava/lang/String; B)":
    "MANAGE_ACCOUNTS",
    "Landroid/accounts/AccountManagerService;-invalidateAuthToken-(Ljava/lang/String; Ljava/lang/String;)":
    "MANAGE_ACCOUNTS",
    "Landroid/accounts/AccountManagerService;-removeAccount-(Landroid/accounts/IAccountManagerResponse; Landroid/accounts/Account;)":
    "MANAGE_ACCOUNTS",
    "Landroid/accounts/AccountManagerService;-updateCredentials-(Landroid/accounts/IAccountManagerResponse; Landroid/accounts/Account; Ljava/lang/String; B Landroid/os/Bundle;)":
    "MANAGE_ACCOUNTS",
    "Landroid/accounts/IAccountManager$Stub$Proxy;-addAcount-(Landroid/accounts/IAccountManagerResponse; Ljava/lang/String; Ljava/lang/String; [L[Ljava/lang/Strin; B Landroid/os/Bundle;)":
    "MANAGE_ACCOUNTS",
    "Landroid/accounts/IAccountManager$Stub$Proxy;-clearPassword-(Landroid/accounts/Account;)":
    "MANAGE_ACCOUNTS",
    "Landroid/accounts/IAccountManager$Stub$Proxy;-confirmCredentials-(Landroid/accounts/IAccountManagerResponse; Landroid/accounts/Account; Landroid/os/Bundle; B)":
    "MANAGE_ACCOUNTS",
    "Landroid/accounts/IAccountManager$Stub$Proxy;-editProperties-(Landroid/accounts/IAccountManagerResponse; Ljava/lang/String; B)":
    "MANAGE_ACCOUNTS",
    "Landroid/accounts/IAccountManager$Stub$Proxy;-invalidateAuthToken-(Ljava/lang/String; Ljava/lang/String;)":
    "MANAGE_ACCOUNTS",
    "Landroid/accounts/IAccountManager$Stub$Proxy;-removeAccount-(Landroid/accounts/IAccountManagerResponse; Landroid/accounts/Account;)":
    "MANAGE_ACCOUNTS",
    "Landroid/accounts/IAccountManager$Stub$Proxy;-updateCredentials-(Landroid/accounts/IAccountManagerResponse; Landroid/accounts/Account; Ljava/lang/String; B Landroid/os/Bundle;)":
    "MANAGE_ACCOUNTS",
    "Landroid/provider/Calendar$CalendarAlerts;-insert-(Landroid/content/ContentResolver; J J J J I)":
    "WRITE_CALENDAR",
    "Landroid/provider/Calendar$Calendars;-delete-(Landroid/content/ContentResolver; Ljava/lang/String; [L[Ljava/lang/Strin;)":
    "WRITE_CALENDAR",
    "Landroid/provider/Calendar$Calendars;-deleteCalendarsForAccount-(Landroid/content/ContentResolver; Landroid/accounts/Account;)":
    "WRITE_CALENDAR",
    "Landroid/appwidget/AppWidgetManager;-bindAppWidgetId-(I Landroid/content/ComponentName;)":
    "BIND_APPWIDGET",
    "Lcom/android/internal/appwidget/IAppWidgetService$Stub$Proxy;-bindAppWidgetId-(I LComponentName;)":
    "BIND_APPWIDGET",
    "Landroid/os/storage/IMountService$Stub$Proxy;-mountSecureContainer-(Ljava/lang/String; Ljava/lang/String; I)":
    "ASEC_MOUNT_UNMOUNT",
    "Landroid/os/storage/IMountService$Stub$Proxy;-unmountSecureContainer-(Ljava/lang/String; B)":
    "ASEC_MOUNT_UNMOUNT",
    "Landroid/app/ContextImpl$ApplicationPackageManager;-addPreferredActivity-(LIntentFilter; I [LComponentName; LComponentName;)":
    "SET_PREFERRED_APPLICATIONS",
    "Landroid/app/ContextImpl$ApplicationPackageManager;-clearPackagePreferredActivities-(Ljava/lang/String;)":
    "SET_PREFERRED_APPLICATIONS",
    "Landroid/app/ContextImpl$ApplicationPackageManager;-replacePreferredActivity-(LIntentFilter; I [LComponentName; LComponentName;)":
    "SET_PREFERRED_APPLICATIONS",
    "Landroid/app/ContextImpl$ApplicationPackageManager;-addPreferredActivity-(Landroid/content/IntentFilter; I [Landroid/content/ComponentName; Landroid/content/ComponentName;)":
    "SET_PREFERRED_APPLICATIONS",
    "Landroid/app/ContextImpl$ApplicationPackageManager;-clearPackagePreferredActivities-(Ljava/lang/String;)":
    "SET_PREFERRED_APPLICATIONS",
    "Landroid/app/ContextImpl$ApplicationPackageManager;-replacePreferredActivity-(Landroid/content/IntentFilter; I [Landroid/content/ComponentName; Landroid/content/ComponentName;)":
    "SET_PREFERRED_APPLICATIONS",
    "Landroid/content/pm/PackageManager;-addPreferredActivity-(Landroid/content/IntentFilter; I [Landroid/content/ComponentName; Landroid/content/ComponentName;)":
    "SET_PREFERRED_APPLICATIONS",
    "Landroid/content/pm/PackageManager;-clearPackagePreferredActivities-(Ljava/lang/String;)":
    "SET_PREFERRED_APPLICATIONS",
    "Landroid/content/pm/PackageManager;-replacePreferredActivity-(Landroid/content/IntentFilter; I [Landroid/content/ComponentName; Landroid/content/ComponentName;)":
    "SET_PREFERRED_APPLICATIONS",
    "Landroid/content/pm/IPackageManager$Stub$Proxy;-addPreferredActivity-(Landroid/content/IntentFilter; I [L[Landroid/content/ComponentNam; Landroid/content/ComponentName;)":
    "SET_PREFERRED_APPLICATIONS",
    "Landroid/content/pm/IPackageManager$Stub$Proxy;-clearPackagePreferredActivities-(Ljava/lang/String;)":
    "SET_PREFERRED_APPLICATIONS",
    "Landroid/content/pm/IPackageManager$Stub$Proxy;-replacePreferredActivity-(Landroid/content/IntentFilter; I [L[Landroid/content/ComponentNam; Landroid/content/ComponentName;)":
    "SET_PREFERRED_APPLICATIONS",
    "Landroid/inputmethodservice/InputMethodService;-SoftInputView-I": "NFC",
    "Landroid/inputmethodservice/InputMethodService;-CandidatesView-I": "NFC",
    "Landroid/inputmethodservice/InputMethodService;-FullscreenMode-I": "NFC",
    "Landroid/inputmethodservice/InputMethodService;-GeneratingText-I": "NFC",
    "Landroid/nfc/tech/NfcA;-close-()": "NFC",
    "Landroid/nfc/tech/NfcA;-connect-()": "NFC",
    "Landroid/nfc/tech/NfcA;-get-(Landroid/nfc/Tag;)": "NFC",
    "Landroid/nfc/tech/NfcA;-transceive-([B)": "NFC",
    "Landroid/nfc/tech/NfcB;-close-()": "NFC",
    "Landroid/nfc/tech/NfcB;-connect-()": "NFC",
    "Landroid/nfc/tech/NfcB;-get-(Landroid/nfc/Tag;)": "NFC",
    "Landroid/nfc/tech/NfcB;-transceive-([B)": "NFC",
    "Landroid/nfc/NfcAdapter;-ACTION_TECH_DISCOVERED-Ljava/lang/String;": "NFC",
    "Landroid/nfc/NfcAdapter;-disableForegroundDispatch-(Landroid/app/Activity;)":
    "NFC",
    "Landroid/nfc/NfcAdapter;-disableForegroundNdefPush-(Landroid/app/Activity;)":
    "NFC",
    "Landroid/nfc/NfcAdapter;-enableForegroundDispatch-(Landroid/app/Activity; Landroid/app/PendingIntent; [Landroid/content/IntentFilter; [[Ljava/lang/Stringcollections.deque();)":
    "NFC",
    "Landroid/nfc/NfcAdapter;-enableForegroundNdefPush-(Landroid/app/Activity; Landroid/nfc/NdefMessage;)":
    "NFC",
    "Landroid/nfc/NfcAdapter;-getDefaultAdapter-()": "NFC",
    "Landroid/nfc/NfcAdapter;-getDefaultAdapter-(Landroid/content/Context;)": "NFC",
    "Landroid/nfc/NfcAdapter;-isEnabled-()": "NFC",
    "Landroid/nfc/tech/NfcF;-close-()": "NFC",
    "Landroid/nfc/tech/NfcF;-connect-()": "NFC",
    "Landroid/nfc/tech/NfcF;-get-(Landroid/nfc/Tag;)": "NFC",
    "Landroid/nfc/tech/NfcF;-transceive-([B)": "NFC",
    "Landroid/nfc/tech/NdefFormatable;-close-()": "NFC",
    "Landroid/nfc/tech/NdefFormatable;-connect-()": "NFC",
    "Landroid/nfc/tech/NdefFormatable;-format-(Landroid/nfc/NdefMessage;)": "NFC",
    "Landroid/nfc/tech/NdefFormatable;-formatReadOnly-(Landroid/nfc/NdefMessage;)":
    "NFC",
    "Landroid/app/Activity;-Fragments-I": "NFC",
    "Landroid/app/Activity;-ActivityLifecycle-I": "NFC",
    "Landroid/app/Activity;-ConfigurationChanges-I": "NFC",
    "Landroid/app/Activity;-StartingActivities-I": "NFC",
    "Landroid/app/Activity;-SavingPersistentState-I": "NFC",
    "Landroid/app/Activity;-Permissions-I": "NFC",
    "Landroid/app/Activity;-ProcessLifecycle-I": "NFC",
    "Landroid/nfc/tech/MifareClassic;-KEY_NFC_FORUM-[B": "NFC",
    "Landroid/nfc/tech/MifareClassic;-authenticateSectorWithKeyA-(I [B)": "NFC",
    "Landroid/nfc/tech/MifareClassic;-authenticateSectorWithKeyB-(I [B)": "NFC",
    "Landroid/nfc/tech/MifareClassic;-close-()": "NFC",
    "Landroid/nfc/tech/MifareClassic;-connect-()": "NFC",
    "Landroid/nfc/tech/MifareClassic;-decrement-(I I)": "NFC",
    "Landroid/nfc/tech/MifareClassic;-increment-(I I)": "NFC",
    "Landroid/nfc/tech/MifareClassic;-readBlock-(I)": "NFC",
    "Landroid/nfc/tech/MifareClassic;-restore-(I)": "NFC",
    "Landroid/nfc/tech/MifareClassic;-transceive-([B)": "NFC",
    "Landroid/nfc/tech/MifareClassic;-transfer-(I)": "NFC",
    "Landroid/nfc/tech/MifareClassic;-writeBlock-(I [B)": "NFC",
    "Landroid/nfc/Tag;-getTechList-()": "NFC",
    "Landroid/app/Service;-WhatIsAService-I": "NFC",
    "Landroid/app/Service;-ServiceLifecycle-I": "NFC",
    "Landroid/app/Service;-Permissions-I": "NFC",
    "Landroid/app/Service;-ProcessLifecycle-I": "NFC",
    "Landroid/app/Service;-LocalServiceSample-I": "NFC",
    "Landroid/app/Service;-RemoteMessengerServiceSample-I": "NFC",
    "Landroid/nfc/NfcManager;-getDefaultAdapter-()": "NFC",
    "Landroid/nfc/tech/MifareUltralight;-close-()": "NFC",
    "Landroid/nfc/tech/MifareUltralight;-connect-()": "NFC",
    "Landroid/nfc/tech/MifareUltralight;-readPages-(I)": "NFC",
    "Landroid/nfc/tech/MifareUltralight;-transceive-([B)": "NFC",
    "Landroid/nfc/tech/MifareUltralight;-writePage-(I [B)": "NFC",
    "Landroid/nfc/tech/NfcV;-close-()": "NFC",
    "Landroid/nfc/tech/NfcV;-connect-()": "NFC",
    "Landroid/nfc/tech/NfcV;-get-(Landroid/nfc/Tag;)": "NFC",
    "Landroid/nfc/tech/NfcV;-transceive-([B)": "NFC",
    "Landroid/nfc/tech/TagTechnology;-close-()": "NFC",
    "Landroid/nfc/tech/TagTechnology;-connect-()": "NFC",
    "Landroid/preference/PreferenceActivity;-SampleCode-Ljava/lang/String;": "NFC",
    "Landroid/content/pm/PackageManager;-FEATURE_NFC-Ljava/lang/String;": "NFC",
    "Landroid/content/Context;-NFC_SERVICE-Ljava/lang/String;": "NFC",
    "Landroid/nfc/tech/Ndef;-NFC_FORUM_TYPE_1-Ljava/lang/String;": "NFC",
    "Landroid/nfc/tech/Ndef;-NFC_FORUM_TYPE_2-Ljava/lang/String;": "NFC",
    "Landroid/nfc/tech/Ndef;-NFC_FORUM_TYPE_3-Ljava/lang/String;": "NFC",
    "Landroid/nfc/tech/Ndef;-NFC_FORUM_TYPE_4-Ljava/lang/String;": "NFC",
    "Landroid/nfc/tech/Ndef;-close-()": "NFC",
    "Landroid/nfc/tech/Ndef;-connect-()": "NFC",
    "Landroid/nfc/tech/Ndef;-getType-()": "NFC",
    "Landroid/nfc/tech/Ndef;-isWritable-()": "NFC",
    "Landroid/nfc/tech/Ndef;-makeReadOnly-()": "NFC",
    "Landroid/nfc/tech/Ndef;-writeNdefMessage-(Landroid/nfc/NdefMessage;)": "NFC",
    "Landroid/nfc/tech/IsoDep;-close-()": "NFC",
    "Landroid/nfc/tech/IsoDep;-connect-()": "NFC",
    "Landroid/nfc/tech/IsoDep;-setTimeout-(I)": "NFC",
    "Landroid/nfc/tech/IsoDep;-transceive-([B)": "NFC",
    "Lcom/android/internal/telephony/ITelephony$Stub$Proxy;-call-(Ljava/lang/String;)":
    "CALL_PHONE",
    "Lcom/android/internal/telephony/ITelephony$Stub$Proxy;-endCall-()": "CALL_PHONE",
    "Lcom/android/http/multipart/FilePart;-sendData-(Ljava/io/OutputStream;)":
    "INTERNET",
    "Lcom/android/http/multipart/FilePart;-sendDispositionHeader-(Ljava/io/OutputStream;)":
    "INTERNET",
    "Ljava/net/HttpURLConnection;-<init>-(Ljava/net/URL;)": "INTERNET",
    "Ljava/net/HttpURLConnection;-connect-()": "INTERNET",
    "Landroid/webkit/WebSettings;-setBlockNetworkLoads-(B)": "INTERNET",
    "Landroid/webkit/WebSettings;-verifyNetworkAccess-()": "INTERNET",
    "Lorg/apache/http/impl/client/DefaultHttpClient;-<init>-()": "INTERNET",
    "Lorg/apache/http/impl/client/DefaultHttpClient;-<init>-(Lorg/apache/http/params/HttpParams;)":
    "INTERNET",
    "Lorg/apache/http/impl/client/DefaultHttpClient;-<init>-(Lorg/apache/http/conn/ClientConnectionManager; Lorg/apache/http/params/HttpParams;)":
    "INTERNET",
    "Lorg/apache/http/impl/client/DefaultHttpClient;-execute-(Lorg/apache/http/client/methods/HttpUriRequest;)":
    "INTERNET",
    "Lorg/apache/http/impl/client/DefaultHttpClient;-execute-(Lorg/apache/http/client/methods/HttpUriRequest; Lorg/apache/http/client/ResponseHandler; Lorg/apache/http/protocol/HttpContext;)":
    "INTERNET",
    "Lorg/apache/http/impl/client/DefaultHttpClient;-execute-(Lorg/apache/http/HttpHost; Lorg/apache/http/client/methods/HttpUriRequest; Lorg/apache/http/client/ResponseHandler; Lorg/apache/http/protocol/HttpContext;)":
    "INTERNET",
    "Lorg/apache/http/impl/client/DefaultHttpClient;-execute-(Lorg/apache/http/client/methods/HttpUriRequest; Lorg/apache/http/protocol/HttpContext;)":
    "INTERNET",
    "Lorg/apache/http/impl/client/DefaultHttpClient;-execute-(Lorg/apache/http/client/methods/HttpUriRequest; Lorg/apache/http/client/ResponseHandler;)":
    "INTERNET",
    "Lorg/apache/http/impl/client/DefaultHttpClient;-execute-(Lorg/apache/http/HttpHost; Lorg/apache/http/client/methods/HttpUriRequest; Lorg/apache/http/client/ResponseHandler;)":
    "INTERNET",
    "Lorg/apache/http/impl/client/DefaultHttpClient;-execute-(Lorg/apache/http/HttpHost; Lorg/apache/http/client/methods/HttpUriRequest;)":
    "INTERNET",
    "Lorg/apache/http/impl/client/DefaultHttpClient;-execute-(Lorg/apache/http/HttpHost; Lorg/apache/http/client/methods/HttpUriRequest; Lorg/apache/http/protocol/HttpContext;)":
    "INTERNET",
    "Lorg/apache/http/impl/client/HttpClient;-execute-(Lorg/apache/http/client/methods/HttpUriRequest;)":
    "INTERNET",
    "Lorg/apache/http/impl/client/HttpClient;-execute-(Lorg/apache/http/client/methods/HttpUriRequest; Lorg/apache/http/client/ResponseHandler; Lorg/apache/http/protocol/HttpContext;)":
    "INTERNET",
    "Lorg/apache/http/impl/client/HttpClient;-execute-(Lorg/apache/http/HttpHost; Lorg/apache/http/client/methods/HttpUriRequest; Lorg/apache/http/client/ResponseHandler; Lorg/apache/http/protocol/HttpContext;)":
    "INTERNET",
    "Lorg/apache/http/impl/client/HttpClient;-execute-(Lorg/apache/http/client/methods/HttpUriRequest; Lorg/apache/http/protocol/HttpContext;)":
    "INTERNET",
    "Lorg/apache/http/impl/client/HttpClient;-execute-(Lorg/apache/http/client/methods/HttpUriRequest; Lorg/apache/http/client/ResponseHandler;)":
    "INTERNET",
    "Lorg/apache/http/impl/client/HttpClient;-execute-(Lorg/apache/http/HttpHost; Lorg/apache/http/client/methods/HttpUriRequest; Lorg/apache/http/client/ResponseHandler;)":
    "INTERNET",
    "Lorg/apache/http/impl/client/HttpClient;-execute-(Lorg/apache/http/HttpHost; Lorg/apache/http/client/methods/HttpUriRequest;)":
    "INTERNET",
    "Lorg/apache/http/impl/client/HttpClient;-execute-(Lorg/apache/http/HttpHost; Lorg/apache/http/client/methods/HttpUriRequest; Lorg/apache/http/protocol/HttpContext;)":
    "INTERNET",
    "Lcom/android/http/multipart/Part;-send-(Ljava/io/OutputStream;)": "INTERNET",
    "Lcom/android/http/multipart/Part;-sendParts-(Ljava/io/OutputStream; [Lcom/android/http/multipart/Part;)":
    "INTERNET",
    "Lcom/android/http/multipart/Part;-sendParts-(Ljava/io/OutputStream; [Lcom/android/http/multipart/Part; [B)":
    "INTERNET",
    "Lcom/android/http/multipart/Part;-sendStart-(Ljava/io/OutputStream;)": "INTERNET",
    "Lcom/android/http/multipart/Part;-sendTransferEncodingHeader-(Ljava/io/OutputStream;)":
    "INTERNET",
    "Landroid/drm/DrmErrorEvent;-TYPE_NO_INTERNET_CONNECTION-I": "INTERNET",
    "Landroid/webkit/WebViewCore;-<init>-(Landroid/content/Context; Landroid/webkit/WebView; Landroid/webkit/CallbackProxy; Ljava/util/Map;)":
    "INTERNET",
    "Ljava/net/URLConnection;-connect-()": "INTERNET",
    "Ljava/net/URLConnection;-getInputStream-()": "INTERNET",
    "Landroid/app/Activity;-setContentView-(I)": "INTERNET",
    "Ljava/net/MulticastSocket;-<init>-()": "INTERNET",
    "Ljava/net/MulticastSocket;-<init>-(I)": "INTERNET",
    "Ljava/net/MulticastSocket;-<init>-(Ljava/net/SocketAddress;)": "INTERNET",
    "Lcom/android/http/multipart/StringPart;-sendData-(Ljava/io/OuputStream;)":
    "INTERNET",
    "Ljava/net/URL;-getContent-([Ljava/lang/Class;)": "INTERNET",
    "Ljava/net/URL;-getContent-()": "INTERNET",
    "Ljava/net/URL;-openConnection-(Ljava/net/Proxy;)": "INTERNET",
    "Ljava/net/URL;-openConnection-()": "INTERNET",
    "Ljava/net/URL;-openStream-()": "INTERNET",
    "Ljava/net/DatagramSocket;-<init>-()": "INTERNET",
    "Ljava/net/DatagramSocket;-<init>-(I)": "INTERNET",
    "Ljava/net/DatagramSocket;-<init>-(I Ljava/net/InetAddress;)": "INTERNET",
    "Ljava/net/DatagramSocket;-<init>-(Ljava/net/SocketAddress;)": "INTERNET",
    "Ljava/net/ServerSocket;-<init>-()": "INTERNET",
    "Ljava/net/ServerSocket;-<init>-(I)": "INTERNET",
    "Ljava/net/ServerSocket;-<init>-(I I)": "INTERNET",
    "Ljava/net/ServerSocket;-<init>-(I I Ljava/net/InetAddress;)": "INTERNET",
    "Ljava/net/ServerSocket;-bind-(Ljava/net/SocketAddress;)": "INTERNET",
    "Ljava/net/ServerSocket;-bind-(Ljava/net/SocketAddress; I)": "INTERNET",
    "Ljava/net/Socket;-<init>-()": "INTERNET",
    "Ljava/net/Socket;-<init>-(Ljava/lang/String; I)": "INTERNET",
    "Ljava/net/Socket;-<init>-(Ljava/lang/String; I Ljava/net/InetAddress; I)":
    "INTERNET",
    "Ljava/net/Socket;-<init>-(Ljava/lang/String; I B)": "INTERNET",
    "Ljava/net/Socket;-<init>-(Ljava/net/InetAddress; I)": "INTERNET",
    "Ljava/net/Socket;-<init>-(Ljava/net/InetAddress; I Ljava/net/InetAddress; I)":
    "INTERNET",
    "Ljava/net/Socket;-<init>-(Ljava/net/InetAddress; I B)": "INTERNET",
    "Landroid/webkit/WebView;-<init>-(Landroid/content/Context; Landroid/util/AttributeSet; I)":
    "INTERNET",
    "Landroid/webkit/WebView;-<init>-(Landroid/content/Context; Landroid/util/AttributeSet;)":
    "INTERNET",
    "Landroid/webkit/WebView;-<init>-(Landroid/content/Context;)": "INTERNET",
    "Ljava/net/NetworkInterface;-<init>-()": "INTERNET",
    "Ljava/net/NetworkInterface;-<init>-(Ljava/lang/String; I Ljava/net/InetAddress;)":
    "INTERNET",
    "Landroid/webkit/WebChromeClient;-onGeolocationPermissionsShowPrompt-(Ljava/lang/String; Landroid/webkit/GeolocationPermissions/Callback;)":
    "ACCESS_FINE_LOCATION",
    "Landroid/location/LocationManager;-GPS_PROVIDER-Ljava/lang/String;":
    "ACCESS_FINE_LOCATION",
    "Landroid/location/LocationManager;-NETWORK_PROVIDER-Ljava/lang/String;":
    "ACCESS_FINE_LOCATION",
    "Landroid/location/LocationManager;-PASSIVE_PROVIDER-Ljava/lang/String;":
    "ACCESS_FINE_LOCATION",
    "Landroid/location/LocationManager;-addGpsStatusListener-(Landroid/location/GpsStatus/Listener;)":
    "ACCESS_FINE_LOCATION",
    "Landroid/location/LocationManager;-addNmeaListener-(Landroid/location/GpsStatus/NmeaListener;)":
    "ACCESS_FINE_LOCATION",
    "Landroid/location/LocationManager;-_requestLocationUpdates-(Ljava/lang/String; J F Landroid/app/PendingIntent;)":
    "ACCESS_FINE_LOCATION",
    "Landroid/location/LocationManager;-_requestLocationUpdates-(Ljava/lang/String; J F Landroid/location/LocationListener; Landroid/os/Looper;)":
    "ACCESS_FINE_LOCATION",
    "Landroid/location/LocationManager;-addGpsStatusListener-(Landroid/location/GpsStatus$Listener;)":
    "ACCESS_FINE_LOCATION",
    "Landroid/location/LocationManager;-addNmeaListener-(Landroid/location/GpsStatus$NmeaListener;)":
    "ACCESS_FINE_LOCATION",
    "Landroid/location/LocationManager;-addProximityAlert-(D D F J Landroid/app/PendingIntent;)":
    "ACCESS_FINE_LOCATION",
    "Landroid/location/LocationManager;-best-(Ljava/util/List;)":
    "ACCESS_FINE_LOCATION",
    "Landroid/location/LocationManager;-getBestProvider-(Landroid/location/Criteria; B)":
    "ACCESS_FINE_LOCATION",
    "Landroid/location/LocationManager;-getLastKnownLocation-(Ljava/lang/String;)":
    "ACCESS_FINE_LOCATION",
    "Landroid/location/LocationManager;-getProvider-(Ljava/lang/String;)":
    "ACCESS_FINE_LOCATION",
    "Landroid/location/LocationManager;-getProviders-(Landroid/location/Criteria; B)":
    "ACCESS_FINE_LOCATION",
    "Landroid/location/LocationManager;-getProviders-(B)": "ACCESS_FINE_LOCATION",
    "Landroid/location/LocationManager;-isProviderEnabled-(Ljava/lang/String;)":
    "ACCESS_FINE_LOCATION",
    "Landroid/location/LocationManager;-requestLocationUpdates-(Ljava/lang/String; J F Landroid/app/PendingIntent;)":
    "ACCESS_FINE_LOCATION",
    "Landroid/location/LocationManager;-requestLocationUpdates-(Ljava/lang/String; J F Landroid/location/LocationListener; Landroid/os/Looper;)":
    "ACCESS_FINE_LOCATION",
    "Landroid/location/LocationManager;-requestLocationUpdates-(Ljava/lang/String; J F Landroid/location/LocationListener;)":
    "ACCESS_FINE_LOCATION",
    "Landroid/location/LocationManager;-sendExtraCommand-(Ljava/lang/String; Ljava/lang/String; Landroid/os/Bundle;)":
    "ACCESS_FINE_LOCATION",
    "Landroid/webkit/GeolocationService;-registerForLocationUpdates-()":
    "ACCESS_FINE_LOCATION",
    "Landroid/webkit/GeolocationService;-setEnableGps-(B)": "ACCESS_FINE_LOCATION",
    "Landroid/webkit/GeolocationService;-start-()": "ACCESS_FINE_LOCATION",
    "Landroid/telephony/TelephonyManager;-getCellLocation-()": "ACCESS_FINE_LOCATION",
    "Landroid/telephony/TelephonyManager;-getCellLocation-()": "ACCESS_FINE_LOCATION",
    "Landroid/telephony/TelephonyManager;-getNeighboringCellInfo-()":
    "ACCESS_FINE_LOCATION",
    "Landroid/location/ILocationManager$Stub$Proxy;-addGpsStatusListener-(Landroid/location/IGpsStatusListener;)":
    "ACCESS_FINE_LOCATION",
    "Landroid/location/ILocationManager$Stub$Proxy;-addProximityAlert-(D D F J Landroid/app/PendingIntent;)":
    "ACCESS_FINE_LOCATION",
    "Landroid/location/ILocationManager$Stub$Proxy;-getLastKnownLocation-(Ljava/lang/String;)":
    "ACCESS_FINE_LOCATION",
    "Landroid/location/ILocationManager$Stub$Proxy;-getProviderInfo-(Ljava/lang/String;)":
    "ACCESS_FINE_LOCATION",
    "Landroid/location/ILocationManager$Stub$Proxy;-getProviders-(B)":
    "ACCESS_FINE_LOCATION",
    "Landroid/location/ILocationManager$Stub$Proxy;-isProviderEnabled-(Ljava/lang/String;)":
    "ACCESS_FINE_LOCATION",
    "Landroid/location/ILocationManager$Stub$Proxy;-requestLocationUpdates-(Ljava/lang/String; J F Landroid/location/ILocationListener;)":
    "ACCESS_FINE_LOCATION",
    "Landroid/location/ILocationManager$Stub$Proxy;-requestLocationUpdatesPI-(Ljava/lang/String; J F Landroid/app/PendingIntent;)":
    "ACCESS_FINE_LOCATION",
    "Landroid/location/ILocationManager$Stub$Proxy;-sendExtraCommand-(Ljava/lang/String; Ljava/lang/String; Landroid/os/Bundle;)":
    "ACCESS_FINE_LOCATION",
    "Lcom/android/internal/telephony/ITelephony$Stub$Proxy;-getCellLocation-()":
    "ACCESS_FINE_LOCATION",
    "Lcom/android/internal/telephony/ITelephony$Stub$Proxy;-getNeighboringCellInfo-()":
    "ACCESS_FINE_LOCATION",
    "Landroid/webkit/GeolocationPermissions$Callback;-invok-()": "ACCESS_FINE_LOCATION",
    "Landroid/provider/Telephony$Sms$Inbox;-addMessage-(Landroid/content/ContentResolver; Ljava/lang/String; Ljava/lang/String; Ljava/lang/String; Ljava/lang/Long; B)":
    "READ_SMS",
    "Landroid/provider/Telephony$Threads;-getOrCreateThreadId-(Landroid/content/Context; Ljava/lang/String;)":
    "READ_SMS",
    "Landroid/provider/Telephony$Threads;-getOrCreateThreadId-(Landroid/content/Context; Ljava/util/Set;)":
    "READ_SMS",
    "Landroid/provider/Telephony$Mms;-query-(Landroid/content/ContentResolver; [L[Ljava/lang/Strin; Ljava/lang/String; Ljava/lang/String;)":
    "READ_SMS",
    "Landroid/provider/Telephony$Mms;-query-(Landroid/content/ContentResolver; [L[Ljava/lang/Strin;)":
    "READ_SMS",
    "Landroid/provider/Telephony$Sms$Draft;-addMessage-(Landroid/content/ContentResolver; Ljava/lang/String; Ljava/lang/String; Ljava/lang/String; Ljava/lang/Long;)":
    "READ_SMS",
    "Landroid/provider/Telephony$Sms$Sent;-addMessage-(Landroid/content/ContentResolver; Ljava/lang/String; Ljava/lang/String; Ljava/lang/String; Ljava/lang/Long;)":
    "READ_SMS",
    "Landroid/provider/Telephony$Sms;-query-(Landroid/content/ContentResolver; [L[Ljava/lang/Strin; Ljava/lang/String; Ljava/lang/String;)":
    "READ_SMS",
    "Landroid/provider/Telephony$Sms;-query-(Landroid/content/ContentResolver; [L[Ljava/lang/Strin;)":
    "READ_SMS",
    "Landroid/view/SurfaceSession;-<init>-()": "ACCESS_SURFACE_FLINGER",
    "Landroid/view/Surface;-closeTransaction-()": "ACCESS_SURFACE_FLINGER",
    "Landroid/view/Surface;-freezeDisplay-(I)": "ACCESS_SURFACE_FLINGER",
    "Landroid/view/Surface;-setOrientation-(I I I)": "ACCESS_SURFACE_FLINGER",
    "Landroid/view/Surface;-setOrientation-(I I)": "ACCESS_SURFACE_FLINGER",
    "Landroid/view/Surface;-unfreezeDisplay-(I)": "ACCESS_SURFACE_FLINGER",
    "Landroid/app/IActivityManager$Stub$Proxy;-moveTaskBackwards-(I)": "REORDER_TASKS",
    "Landroid/app/IActivityManager$Stub$Proxy;-moveTaskToBack-(I)": "REORDER_TASKS",
    "Landroid/app/IActivityManager$Stub$Proxy;-moveTaskToFront-(I)": "REORDER_TASKS",
    "Landroid/app/ActivityManager;-moveTaskToFront-(I I)": "REORDER_TASKS",
    "Landroid/net/sip/SipAudioCall;-setSpeakerMode-(B)": "MODIFY_AUDIO_SETTINGS",
    "Landroid/server/BluetoothA2dpService;-checkSinkSuspendState-(I)":
    "MODIFY_AUDIO_SETTINGS",
    "Landroid/server/BluetoothA2dpService;-handleSinkStateChange-(Landroid/bluetooth/BluetoothDevice;)":
    "MODIFY_AUDIO_SETTINGS",
    "Landroid/server/BluetoothA2dpService;-onBluetoothDisable-()":
    "MODIFY_AUDIO_SETTINGS",
    "Landroid/server/BluetoothA2dpService;-onBluetoothEnable-()":
    "MODIFY_AUDIO_SETTINGS",
    "Landroid/media/IAudioService$Stub$Proxy;-setBluetoothScoOn-(B)":
    "MODIFY_AUDIO_SETTINGS",
    "Landroid/media/IAudioService$Stub$Proxy;-setMode-(I Landroid/os/IBinder;)":
    "MODIFY_AUDIO_SETTINGS",
    "Landroid/media/IAudioService$Stub$Proxy;-setSpeakerphoneOn-(B)":
    "MODIFY_AUDIO_SETTINGS",
    "Landroid/media/IAudioService$Stub$Proxy;-startBluetoothSco-(Landroid/os/IBinder;)":
    "MODIFY_AUDIO_SETTINGS",
    "Landroid/media/IAudioService$Stub$Proxy;-stopBluetoothSco-(Landroid/os/IBinder;)":
    "MODIFY_AUDIO_SETTINGS",
    "Landroid/media/AudioService;-setBluetoothScoOn-(B)": "MODIFY_AUDIO_SETTINGS",
    "Landroid/media/AudioService;-setMode-(I Landroid/os/IBinder;)":
    "MODIFY_AUDIO_SETTINGS",
    "Landroid/media/AudioService;-setSpeakerphoneOn-(B)": "MODIFY_AUDIO_SETTINGS",
    "Landroid/media/AudioService;-startBluetoothSco-(Landroid/os/IBinder;)":
    "MODIFY_AUDIO_SETTINGS",
    "Landroid/media/AudioService;-stopBluetoothSco-(Landroid/os/IBinder;)":
    "MODIFY_AUDIO_SETTINGS",
    "Landroid/media/AudioManager;-startBluetoothSco-()": "MODIFY_AUDIO_SETTINGS",
    "Landroid/media/AudioManager;-stopBluetoothSco-()": "MODIFY_AUDIO_SETTINGS",
    "Landroid/media/AudioManager;-isBluetoothA2dpOn-()": "MODIFY_AUDIO_SETTINGS",
    "Landroid/media/AudioManager;-isWiredHeadsetOn-()": "MODIFY_AUDIO_SETTINGS",
    "Landroid/media/AudioManager;-setBluetoothScoOn-(B)": "MODIFY_AUDIO_SETTINGS",
    "Landroid/media/AudioManager;-setMicrophoneMute-(B)": "MODIFY_AUDIO_SETTINGS",
    "Landroid/media/AudioManager;-setMode-(I)": "MODIFY_AUDIO_SETTINGS",
    "Landroid/media/AudioManager;-setParameter-(Ljava/lang/String; Ljava/lang/String;)":
    "MODIFY_AUDIO_SETTINGS",
    "Landroid/media/AudioManager;-setParameters-(Ljava/lang/String;)":
    "MODIFY_AUDIO_SETTINGS",
    "Landroid/media/AudioManager;-setSpeakerphoneOn-(B)": "MODIFY_AUDIO_SETTINGS",
    "Landroid/media/AudioManager;-startBluetoothSco-()": "MODIFY_AUDIO_SETTINGS",
    "Landroid/media/AudioManager;-stopBluetoothSco-()": "MODIFY_AUDIO_SETTINGS",
    "Lcom/android/internal/telephony/IPhoneSubInfo$Stub$Proxy;-getDeviceId-()":
    "READ_PHONE_STATE",
    "Lcom/android/internal/telephony/IPhoneSubInfo$Stub$Proxy;-getDeviceSvn-()":
    "READ_PHONE_STATE",
    "Lcom/android/internal/telephony/IPhoneSubInfo$Stub$Proxy;-getIccSerialNumber-()":
    "READ_PHONE_STATE",
    "Lcom/android/internal/telephony/IPhoneSubInfo$Stub$Proxy;-getLine1AlphaTag-()":
    "READ_PHONE_STATE",
    "Lcom/android/internal/telephony/IPhoneSubInfo$Stub$Proxy;-getLine1Number-()":
    "READ_PHONE_STATE",
    "Lcom/android/internal/telephony/IPhoneSubInfo$Stub$Proxy;-getSubscriberId-()":
    "READ_PHONE_STATE",
    "Lcom/android/internal/telephony/IPhoneSubInfo$Stub$Proxy;-getVoiceMailAlphaTag-()":
    "READ_PHONE_STATE",
    "Lcom/android/internal/telephony/IPhoneSubInfo$Stub$Proxy;-getVoiceMailNumber-()":
    "READ_PHONE_STATE",
    "Landroid/telephony/PhoneStateListener;-LISTEN_CALL_FORWARDING_INDICATOR-I":
    "READ_PHONE_STATE",
    "Landroid/telephony/PhoneStateListener;-LISTEN_CALL_STATE-I": "READ_PHONE_STATE",
    "Landroid/telephony/PhoneStateListener;-LISTEN_DATA_ACTIVITY-I": "READ_PHONE_STATE",
    "Landroid/telephony/PhoneStateListener;-LISTEN_MESSAGE_WAITING_INDICATOR-I":
    "READ_PHONE_STATE",
    "Landroid/telephony/PhoneStateListener;-LISTEN_SIGNAL_STRENGTH-I":
    "READ_PHONE_STATE",
    "Landroid/accounts/AccountManagerService$SimWatcher;-onReceive-(Landroid/content/Context; Landroid/content/Intent;)":
    "READ_PHONE_STATE",
    "Lcom/android/internal/telephony/CallerInfo;-markAsVoiceMail-()":
    "READ_PHONE_STATE",
    "Landroid/os/Build/VERSION_CODES;-DONUT-I": "READ_PHONE_STATE",
    "Landroid/telephony/TelephonyManager;-ACTION_PHONE_STATE_CHANGED-Ljava/lang/String;":
    "READ_PHONE_STATE",
    "Landroid/telephony/TelephonyManager;-getDeviceId-()": "READ_PHONE_STATE",
    "Landroid/telephony/TelephonyManager;-getDeviceSoftwareVersion-()":
    "READ_PHONE_STATE",
    "Landroid/telephony/TelephonyManager;-getLine1Number-()": "READ_PHONE_STATE",
    "Landroid/telephony/TelephonyManager;-getSimSerialNumber-()": "READ_PHONE_STATE",
    "Landroid/telephony/TelephonyManager;-getSubscriberId-()": "READ_PHONE_STATE",
    "Landroid/telephony/TelephonyManager;-getVoiceMailAlphaTag-()": "READ_PHONE_STATE",
    "Landroid/telephony/TelephonyManager;-getVoiceMailNumber-()": "READ_PHONE_STATE",
    "Landroid/telephony/TelephonyManager;-getDeviceId-()": "READ_PHONE_STATE",
    "Landroid/telephony/TelephonyManager;-getDeviceSoftwareVersion-()":
    "READ_PHONE_STATE",
    "Landroid/telephony/TelephonyManager;-getLine1AlphaTag-()": "READ_PHONE_STATE",
    "Landroid/telephony/TelephonyManager;-getLine1Number-()": "READ_PHONE_STATE",
    "Landroid/telephony/TelephonyManager;-getSimSerialNumber-()": "READ_PHONE_STATE",
    "Landroid/telephony/TelephonyManager;-getSubscriberId-()": "READ_PHONE_STATE",
    "Landroid/telephony/TelephonyManager;-getVoiceMailAlphaTag-()": "READ_PHONE_STATE",
    "Landroid/telephony/TelephonyManager;-getVoiceMailNumber-()": "READ_PHONE_STATE",
    "Landroid/telephony/TelephonyManager;-listen-(Landroid/telephony/PhoneStateListener; I)":
    "READ_PHONE_STATE",
    "Lcom/android/internal/telephony/ITelephonyRegistry$Stub$Proxy;-listen-(Ljava/lang/String; Lcom/android/internal/telephony/IPhoneStateListener; I B)":
    "READ_PHONE_STATE",
    "Landroid/telephony/PhoneNumberUtils;-isVoiceMailNumber-(Ljava/lang/String;)":
    "READ_PHONE_STATE",
    "Lcom/android/internal/telephony/ITelephony$Stub$Proxy;-isSimPinEnabled-()":
    "READ_PHONE_STATE",
    "Landroid/media/RingtoneManager;-setActualDefaultRingtoneUri-(Landroid/content/Context; I Landroid/net/Uri;)":
    "WRITE_SETTINGS",
    "Landroid/os/IPowerManager$Stub$Proxy;-setStayOnSetting-(I)": "WRITE_SETTINGS",
    "Landroid/server/BluetoothService;-persistBluetoothOnSetting-(B)": "WRITE_SETTINGS",
    "Landroid/provider/Settings$Secure;-putFloat-(Landroid/content/ContentResolver; Ljava/lang/String; F)":
    "WRITE_SETTINGS",
    "Landroid/provider/Settings$Secure;-putInt-(Landroid/content/ContentResolver; Ljava/lang/String; I)":
    "WRITE_SETTINGS",
    "Landroid/provider/Settings$Secure;-putLong-(Landroid/content/ContentResolver; Ljava/lang/String; J)":
    "WRITE_SETTINGS",
    "Landroid/provider/Settings$Secure;-putString-(Landroid/content/ContentResolver; Ljava/lang/String; Ljava/lang/String;)":
    "WRITE_SETTINGS",
    "Landroid/provider/Settings$Secure;-setLocationProviderEnabled-(Landroid/content/ContentResolver; Ljava/lang/String; B)":
    "WRITE_SETTINGS",
    "Landroid/provider/Settings$Bookmarks;-add-(Landroid/content/ContentResolver; Landroid/content/Intent; Ljava/lang/String; Ljava/lang/String; C I)":
    "WRITE_SETTINGS",
    "Landroid/provider/Settings$Bookmarks;-getIntentForShortcut-(Landroid/content/ContentResolver; C)":
    "WRITE_SETTINGS",
    "Landroid/os/IMountService$Stub$Proxy;-setAutoStartUm-()": "WRITE_SETTINGS",
    "Landroid/os/IMountService$Stub$Proxy;-setPlayNotificationSound-()":
    "WRITE_SETTINGS",
    "Landroid/provider/Settings$System;-putConfiguration-(Landroid/content/ContentResolver; Landroid/content/res/Configuration;)":
    "WRITE_SETTINGS",
    "Landroid/provider/Settings$System;-putFloat-(Landroid/content/ContentResolver; Ljava/lang/String; F)":
    "WRITE_SETTINGS",
    "Landroid/provider/Settings$System;-putInt-(Landroid/content/ContentResolver; Ljava/lang/String; I)":
    "WRITE_SETTINGS",
    "Landroid/provider/Settings$System;-putLong-(Landroid/content/ContentResolver; Ljava/lang/String; J)":
    "WRITE_SETTINGS",
    "Landroid/provider/Settings$System;-putString-(Landroid/content/ContentResolver; Ljava/lang/String; Ljava/lang/String;)":
    "WRITE_SETTINGS",
    "Landroid/provider/Settings$System;-setShowGTalkServiceStatus-(Landroid/content/ContentResolver; B)":
    "WRITE_SETTINGS",
    "Landroid/service/wallpaper/WallpaperService;-SERVICE_INTERFACE-Ljava/lang/String;":
    "BIND_WALLPAPER",
    "Lcom/android/server/WallpaperManagerService;-bindWallpaperComponentLocked-(Landroid/content/ComponentName;)":
    "BIND_WALLPAPER",
    "Landroid/content/ContentService;-dump-(Ljava/io/FileDescriptor; Ljava/io/PrintWriter; [L[Ljava/lang/Strin;)":
    "DUMP",
    "Landroid/view/IWindowManager$Stub$Proxy;-isViewServerRunning-()": "DUMP",
    "Landroid/view/IWindowManager$Stub$Proxy;-startViewServer-(I)": "DUMP",
    "Landroid/view/IWindowManager$Stub$Proxy;-stopViewServer-()": "DUMP",
    "Landroid/os/Debug;-dumpService-(Ljava/lang/String; Ljava/io/FileDescriptor; [Ljava/lang/String;)":
    "DUMP",
    "Landroid/os/IBinder;-DUMP_TRANSACTION-I": "DUMP",
    "Lcom/android/server/WallpaperManagerService;-dump-(Ljava/io/FileDescriptor; Ljava/io/PrintWriter; [L[Ljava/lang/Stri;)":
    "DUMP",
    "Landroid/accounts/AccountManager;-blockingGetAuthToken-(Landroid/accounts/Account; Ljava/lang/String; B)":
    "USE_CREDENTIALS",
    "Landroid/accounts/AccountManager;-getAuthToken-(Landroid/accounts/Account; Ljava/lang/String; Landroid/os/Bundle; Landroid/app/Activity; Landroid/accounts/AccountManagerCallback<android/os/Bundle>; Landroid/os/Handler;)":
    "USE_CREDENTIALS",
    "Landroid/accounts/AccountManager;-getAuthToken-(Landroid/accounts/Account; Ljava/lang/String; B Landroid/accounts/AccountManagerCallback<android/os/Bundle>; Landroid/os/Handler;)":
    "USE_CREDENTIALS",
    "Landroid/accounts/AccountManager;-invalidateAuthToken-(Ljava/lang/String; Ljava/lang/String;)":
    "USE_CREDENTIALS",
    "Landroid/accounts/AccountManager;-blockingGetAuthToken-(Landroid/accounts/Account; Ljava/lang/String; B)":
    "USE_CREDENTIALS",
    "Landroid/accounts/AccountManager;-getAuthToken-(Landroid/accounts/Account; Ljava/lang/String; Landroid/os/Bundle; Landroid/app/Activity; Landroid/accounts/AccountManagerCallback; Landroid/os/Handler;)":
    "USE_CREDENTIALS",
    "Landroid/accounts/AccountManager;-getAuthToken-(Landroid/accounts/Account; Ljava/lang/String; B Landroid/accounts/AccountManagerCallback; Landroid/os/Handler;)":
    "USE_CREDENTIALS",
    "Landroid/accounts/AccountManagerService;-getAuthToken-(Landroid/accounts/IAccountManagerResponse; Landroid/accounts/Account; Ljava/lang/String; B B Landroid/os/Bundle;)":
    "USE_CREDENTIALS",
    "Landroid/accounts/IAccountManager$Stub$Proxy;-getAuthToken-(Landroid/accounts/IAccountManagerResponse; Landroid/accounts/Account; Ljava/lang/String; B B Landroid/os/Bundle;)":
    "USE_CREDENTIALS",
    "Lcom/android/internal/app/IUsageStats$Stub$Proxy;-notePauseComponent-(LComponentName;)":
    "UPDATE_DEVICE_STATS",
    "Lcom/android/internal/app/IUsageStats$Stub$Proxy;-noteResumeComponent-(LComponentName;)":
    "UPDATE_DEVICE_STATS",
    "Lcom/android/internal/app/IBatteryStats$Stub$Proxy;-noteFullWifiLockAcquired-(I)":
    "UPDATE_DEVICE_STATS",
    "Lcom/android/internal/app/IBatteryStats$Stub$Proxy;-noteFullWifiLockReleased-(I)":
    "UPDATE_DEVICE_STATS",
    "Lcom/android/internal/app/IBatteryStats$Stub$Proxy;-noteInputEvent-()":
    "UPDATE_DEVICE_STATS",
    "Lcom/android/internal/app/IBatteryStats$Stub$Proxy;-notePhoneDataConnectionState-(I B)":
    "UPDATE_DEVICE_STATS",
    "Lcom/android/internal/app/IBatteryStats$Stub$Proxy;-notePhoneOff-()":
    "UPDATE_DEVICE_STATS",
    "Lcom/android/internal/app/IBatteryStats$Stub$Proxy;-notePhoneOn-()":
    "UPDATE_DEVICE_STATS",
    "Lcom/android/internal/app/IBatteryStats$Stub$Proxy;-notePhoneSignalStrength-(LSignalStrength;)":
    "UPDATE_DEVICE_STATS",
    "Lcom/android/internal/app/IBatteryStats$Stub$Proxy;-notePhoneState-(I)":
    "UPDATE_DEVICE_STATS",
    "Lcom/android/internal/app/IBatteryStats$Stub$Proxy;-noteScanWifiLockAcquired-(I)":
    "UPDATE_DEVICE_STATS",
    "Lcom/android/internal/app/IBatteryStats$Stub$Proxy;-noteScanWifiLockReleased-(I)":
    "UPDATE_DEVICE_STATS",
    "Lcom/android/internal/app/IBatteryStats$Stub$Proxy;-noteScreenBrightness-(I)":
    "UPDATE_DEVICE_STATS",
    "Lcom/android/internal/app/IBatteryStats$Stub$Proxy;-noteScreenOff-()":
    "UPDATE_DEVICE_STATS",
    "Lcom/android/internal/app/IBatteryStats$Stub$Proxy;-noteScreenOn-()":
    "UPDATE_DEVICE_STATS",
    "Lcom/android/internal/app/IBatteryStats$Stub$Proxy;-noteStartGps-(I)":
    "UPDATE_DEVICE_STATS",
    "Lcom/android/internal/app/IBatteryStats$Stub$Proxy;-noteStartSensor-(I I)":
    "UPDATE_DEVICE_STATS",
    "Lcom/android/internal/app/IBatteryStats$Stub$Proxy;-noteStartWakelock-(I Ljava/lang/String; I)":
    "UPDATE_DEVICE_STATS",
    "Lcom/android/internal/app/IBatteryStats$Stub$Proxy;-noteStopGps-(I)":
    "UPDATE_DEVICE_STATS",
    "Lcom/android/internal/app/IBatteryStats$Stub$Proxy;-noteStopSensor-(I I)":
    "UPDATE_DEVICE_STATS",
    "Lcom/android/internal/app/IBatteryStats$Stub$Proxy;-noteStopWakelock-(I Ljava/lang/String; I)":
    "UPDATE_DEVICE_STATS",
    "Lcom/android/internal/app/IBatteryStats$Stub$Proxy;-noteUserActivity-(I I)":
    "UPDATE_DEVICE_STATS",
    "Lcom/android/internal/app/IBatteryStats$Stub$Proxy;-noteWifiMulticastDisabled-(I)":
    "UPDATE_DEVICE_STATS",
    "Lcom/android/internal/app/IBatteryStats$Stub$Proxy;-noteWifiMulticastEnabled-(I)":
    "UPDATE_DEVICE_STATS",
    "Lcom/android/internal/app/IBatteryStats$Stub$Proxy;-noteWifiOff-(I)":
    "UPDATE_DEVICE_STATS",
    "Lcom/android/internal/app/IBatteryStats$Stub$Proxy;-noteWifiOn-(I)":
    "UPDATE_DEVICE_STATS",
    "Lcom/android/internal/app/IBatteryStats$Stub$Proxy;-noteWifiRunning-()":
    "UPDATE_DEVICE_STATS",
    "Lcom/android/internal/app/IBatteryStats$Stub$Proxy;-noteWifiStopped-()":
    "UPDATE_DEVICE_STATS",
    "Lcom/android/internal/app/IBatteryStats$Stub$Proxy;-recordCurrentLevel-(I)":
    "UPDATE_DEVICE_STATS",
    "Lcom/android/internal/app/IBatteryStats$Stub$Proxy;-setOnBattery-(B I)":
    "UPDATE_DEVICE_STATS",
    "Landroid/telephony/gsm/SmsManager;-getDefault-()": "SEND_SMS",
    "Landroid/telephony/gsm/SmsManager;-sendDataMessage-(Ljava/lang/String; Ljava/lang/String; S [B Landroid/app/PendingIntent; Landroid/app/PendingIntent;)":
    "SEND_SMS",
    "Landroid/telephony/gsm/SmsManager;-sendTextMessage-(Ljava/lang/String; Ljava/lang/String; Ljava/lang/String; Landroid/app/PendingIntent; Landroid/app/PendingIntent;)":
    "SEND_SMS",
    "Landroid/telephony/gsm/SmsManager;-sendDataMessage-(Ljava/lang/String; Ljava/lang/String; S [L; Landroid/app/PendingIntent; Landroid/app/PendingIntent;)":
    "SEND_SMS",
    "Landroid/telephony/gsm/SmsManager;-sendMultipartTextMessage-(Ljava/lang/String; Ljava/lang/String; Ljava/util/ArrayList; Ljava/util/ArrayList; Ljava/util/ArrayList;)":
    "SEND_SMS",
    "Landroid/telephony/gsm/SmsManager;-sendTextMessage-(Ljava/lang/String; Ljava/lang/String; Ljava/lang/String; Landroid/app/PendingIntent; Landroid/app/PendingIntent;)":
    "SEND_SMS",
    "Landroid/telephony/SmsManager;-getDefault-()": "SEND_SMS",
    "Landroid/telephony/SmsManager;-sendDataMessage-(Ljava/lang/String; Ljava/lang/String; S [B Landroid/app/PendingIntent; Landroid/app/PendingIntent;)":
    "SEND_SMS",
    "Landroid/telephony/SmsManager;-sendTextMessage-(Ljava/lang/String; Ljava/lang/String; Ljava/lang/String; Landroid/app/PendingIntent; Landroid/app/PendingIntent;)":
    "SEND_SMS",
    "Landroid/telephony/SmsManager;-sendDataMessage-(Ljava/lang/String; Ljava/lang/String; S [L; Landroid/app/PendingIntent; Landroid/app/PendingIntent;)":
    "SEND_SMS",
    "Landroid/telephony/SmsManager;-sendMultipartTextMessage-(Ljava/lang/String; Ljava/lang/String; Ljava/util/ArrayList; Ljava/util/ArrayList; Ljava/util/ArrayList;)":
    "SEND_SMS",
    "Landroid/telephony/SmsManager;-sendTextMessage-(Ljava/lang/String; Ljava/lang/String; Ljava/lang/String; Landroid/app/PendingIntent; Landroid/app/PendingIntent;)":
    "SEND_SMS",
    "Lcom/android/internal/telephony/ISms$Stub$Proxy;-sendData-(Ljava/lang/String; Ljava/lang/String; I [B Landroid/app/PendingIntent; Landroid/app/PendingIntent;)":
    "SEND_SMS",
    "Lcom/android/internal/telephony/ISms$Stub$Proxy;-sendMultipartText-(Ljava/lang/String; Ljava/lang/String; Ljava/util/List; Ljava/util/List; Ljava/util/List;)":
    "SEND_SMS",
    "Lcom/android/internal/telephony/ISms$Stub$Proxy;-sendText-(Ljava/lang/String; Ljava/lang/String; Ljava/lang/String; Landroid/app/PendingIntent; Landroid/app/PendingIntent;)":
    "SEND_SMS",
    "Landroid/provider/UserDictionary$Words;-addWord-(Landroid/content/Context; Ljava/lang/String; I I)":
    "WRITE_USER_DICTIONARY",
    "Landroid/telephony/TelephonyManager;-getCellLocation-()": "ACCESS_COARSE_LOCATION",
    "Landroid/telephony/PhoneStateListener;-LISTEN_CELL_LOCATION-I":
    "ACCESS_COARSE_LOCATION",
    "Landroid/location/LocationManager;-NETWORK_PROVIDER-Ljava/lang/String;":
    "ACCESS_COARSE_LOCATION",
    "Landroid/os/storage/IMountService$Stub$Proxy;-renameSecureContainer-(Ljava/lang/String; Ljava/lang/String;)":
    "ASEC_RENAME",
    "Landroid/view/IWindowSession$Stub$Proxy;-add-(Landroid/view/IWindow; Landroid/view/WindowManager$LayoutParams; I Landroid/graphics/Rect;)":
    "SYSTEM_ALERT_WINDOW",
    "Landroid/net/wifi/IWifiManager$Stub$Proxy;-acquireMulticastLock-(Landroid/os/IBinder; Ljava/lang/String;)":
    "CHANGE_WIFI_MULTICAST_STATE",
    "Landroid/net/wifi/IWifiManager$Stub$Proxy;-initializeMulticastFiltering-()":
    "CHANGE_WIFI_MULTICAST_STATE",
    "Landroid/net/wifi/IWifiManager$Stub$Proxy;-releaseMulticastLock-()":
    "CHANGE_WIFI_MULTICAST_STATE",
    "Landroid/net/wifi/WifiManager$MulticastLock;-acquire-()":
    "CHANGE_WIFI_MULTICAST_STATE",
    "Landroid/net/wifi/WifiManager$MulticastLock;-finalize-()":
    "CHANGE_WIFI_MULTICAST_STATE",
    "Landroid/net/wifi/WifiManager$MulticastLock;-release-()":
    "CHANGE_WIFI_MULTICAST_STATE",
    "Landroid/net/wifi/WifiManager;-initializeMulticastFiltering-()":
    "CHANGE_WIFI_MULTICAST_STATE",
    "Landroid/content/Intent;-ACTION_BOOT_COMPLETED-Ljava/lang/String;":
    "RECEIVE_BOOT_COMPLETED",
    "Landroid/provider/AlarmClock;-ACTION_SET_ALARM-Ljava/lang/String;": "SET_ALARM",
    "Landroid/provider/AlarmClock;-EXTRA_HOUR-Ljava/lang/String;": "SET_ALARM",
    "Landroid/provider/AlarmClock;-EXTRA_MESSAGE-Ljava/lang/String;": "SET_ALARM",
    "Landroid/provider/AlarmClock;-EXTRA_MINUTES-Ljava/lang/String;": "SET_ALARM",
    "Landroid/provider/AlarmClock;-EXTRA_SKIP_UI-Ljava/lang/String;": "SET_ALARM",
    "Lcom/android/internal/telephony/IccPhoneBookInterfaceManager$Stub$Proxy;-updateAdnRecordsInEfByIndex-(I Ljava/lang/String; Ljava/lang/String; Ljava/lang/String;)":
    "WRITE_CONTACTS",
    "Lcom/android/internal/telephony/IccPhoneBookInterfaceManager$Stub$Proxy;-updateAdnRecordsInEfBySearch-(I Ljava/lang/String; Ljava/lang/String; Ljava/lang/String; Ljava/lang/String; Ljava/lang/String;)":
    "WRITE_CONTACTS",
    "Landroid/provider/Contacts$People;-addToGroup-(Landroid/content/ContentResolver; J J)":
    "WRITE_CONTACTS",
    "Landroid/provider/ContactsContract$Contacts;-markAsContacted-(Landroid/content/ContentResolver; J)":
    "WRITE_CONTACTS",
    "Landroid/provider/Contacts$Settings;-setSetting-(Landroid/content/ContentResolver; Ljava/lang/String; Ljava/lang/String; Ljava/lang/String;)":
    "WRITE_CONTACTS",
    "Lcom/android/internal/telephony/IIccPhoneBook$Stub$Proxy;-updateAdnRecordsInEfByIndex-(I Ljava/lang/String; Ljava/lang/String; Ljava/lang/String;)":
    "WRITE_CONTACTS",
    "Lcom/android/internal/telephony/IIccPhoneBook$Stub$Proxy;-updateAdnRecordsInEfBySearch-(I Ljava/lang/String; Ljava/lang/String; Ljava/lang/String; Ljava/lang/String; Ljava/lang/String;)":
    "WRITE_CONTACTS",
    "Landroid/provider/CallLog$Calls;-removeExpiredEntries-(Landroid/content/Context;)":
    "WRITE_CONTACTS",
    "Landroid/pim/vcard/VCardEntryCommitter;-onEntryCreated-(Landroid/pim/vcard/VCardEntry;)":
    "WRITE_CONTACTS",
    "Landroid/pim/vcard/VCardEntryHandler;-onEntryCreated-(Landroid/pim/vcard/VCardEntry;)":
    "WRITE_CONTACTS",
    "Landroid/pim/vcard/VCardEntry;-pushIntoContentResolver-(Landroid/content/ContentResolver;)":
    "WRITE_CONTACTS",
    "Landroid/content/Intent;-ACTION_NEW_OUTGOING_CALL-Ljava/lang/String;":
    "PROCESS_OUTGOING_CALLS",
    "Landroid/app/StatusBarManager;-collapse-()": "EXPAND_STATUS_BAR",
    "Landroid/app/StatusBarManager;-expand-()": "EXPAND_STATUS_BAR",
    "Landroid/app/StatusBarManager;-toggle-()": "EXPAND_STATUS_BAR",
    "Landroid/app/IStatusBar$Stub$Proxy;-activate-()": "EXPAND_STATUS_BAR",
    "Landroid/app/IStatusBar$Stub$Proxy;-deactivate-()": "EXPAND_STATUS_BAR",
    "Landroid/app/IStatusBar$Stub$Proxy;-toggle-()": "EXPAND_STATUS_BAR",
    "Lcom/android/internal/telephony/ITelephony$Stub$Proxy;-answerRingingCall-()":
    "MODIFY_PHONE_STATE",
    "Lcom/android/internal/telephony/ITelephony$Stub$Proxy;-cancelMissedCallsNotification-()":
    "MODIFY_PHONE_STATE",
    "Lcom/android/internal/telephony/ITelephony$Stub$Proxy;-disableApnType-(Ljava/lang/String;)":
    "MODIFY_PHONE_STATE",
    "Lcom/android/internal/telephony/ITelephony$Stub$Proxy;-disableDataConnectivity-()":
    "MODIFY_PHONE_STATE",
    "Lcom/android/internal/telephony/ITelephony$Stub$Proxy;-enableApnType-(Ljava/lang/String;)":
    "MODIFY_PHONE_STATE",
    "Lcom/android/internal/telephony/ITelephony$Stub$Proxy;-enableDataConnectivity-()":
    "MODIFY_PHONE_STATE",
    "Lcom/android/internal/telephony/ITelephony$Stub$Proxy;-handlePinMmi-(Ljava/lang/String;)":
    "MODIFY_PHONE_STATE",
    "Lcom/android/internal/telephony/ITelephony$Stub$Proxy;-setRadio-(B)":
    "MODIFY_PHONE_STATE",
    "Lcom/android/internal/telephony/ITelephony$Stub$Proxy;-silenceRinger-()":
    "MODIFY_PHONE_STATE",
    "Lcom/android/internal/telephony/ITelephony$Stub$Proxy;-supplyPin-(Ljava/lang/String;)":
    "MODIFY_PHONE_STATE",
    "Lcom/android/internal/telephony/ITelephony$Stub$Proxy;-toggleRadioOnOff-()":
    "MODIFY_PHONE_STATE",
    "Landroid/net/MobileDataStateTracker;-reconnect-()": "MODIFY_PHONE_STATE",
    "Landroid/net/MobileDataStateTracker;-setRadio-(B)": "MODIFY_PHONE_STATE",
    "Landroid/net/MobileDataStateTracker;-teardown-()": "MODIFY_PHONE_STATE",
    "Lcom/android/internal/telephony/ITelephonyRegistry$Stub$Proxy;-notifyCallForwardingChanged-(B)":
    "MODIFY_PHONE_STATE",
    "Lcom/android/internal/telephony/ITelephonyRegistry$Stub$Proxy;-notifyCallState-(I Ljava/lang/String;)":
    "MODIFY_PHONE_STATE",
    "Lcom/android/internal/telephony/ITelephonyRegistry$Stub$Proxy;-notifyCellLocation-(Landroid/os/Bundle;)":
    "MODIFY_PHONE_STATE",
    "Lcom/android/internal/telephony/ITelephonyRegistry$Stub$Proxy;-notifyDataActivity-(I)":
    "MODIFY_PHONE_STATE",
    "Lcom/android/internal/telephony/ITelephonyRegistry$Stub$Proxy;-notifyDataConnection-(I B Ljava/lang/String; Ljava/lang/String; [Ljava/lang/String; Ljava/lang/String; I)":
    "MODIFY_PHONE_STATE",
    "Lcom/android/internal/telephony/ITelephonyRegistry$Stub$Proxy;-notifyDataConnectionFailed-(Ljava/lang/String;)":
    "MODIFY_PHONE_STATE",
    "Lcom/android/internal/telephony/ITelephonyRegistry$Stub$Proxy;-notifyMessageWaitingChanged-(B)":
    "MODIFY_PHONE_STATE",
    "Lcom/android/internal/telephony/ITelephonyRegistry$Stub$Proxy;-notifyServiceState-(Landroid/telephony/ServiceState;)":
    "MODIFY_PHONE_STATE",
    "Lcom/android/internal/telephony/ITelephonyRegistry$Stub$Proxy;-notifySignalStrength-(Landroid/telephony/SignalStrength;)":
    "MODIFY_PHONE_STATE",
    "Landroid/os/IMountService$Stub$Proxy;-formatMedi-()": "MOUNT_FORMAT_FILESYSTEMS",
    "Landroid/os/storage/IMountService$Stub$Proxy;-formatVolume-(Ljava/lang/String;)":
    "MOUNT_FORMAT_FILESYSTEMS",
    "Landroid/net/Downloads$DownloadBase;-startDownloadByUri-(Landroid/content/Context; Ljava/lang/String; Ljava/lang/String; B I B B Ljava/lang/String; Ljava/lang/String; Ljava/lang/String; Ljava/lang/String;)":
    "ACCESS_DOWNLOAD_MANAGER",
    "Landroid/net/Downloads$ByUri;-getCurrentOtaDownloads-(Landroid/content/Context; Ljava/lang/String;)":
    "ACCESS_DOWNLOAD_MANAGER",
    "Landroid/net/Downloads$ByUri;-getProgressCursor-(Landroid/content/Context; J)":
    "ACCESS_DOWNLOAD_MANAGER",
    "Landroid/net/Downloads$ByUri;-getStatus-(Landroid/content/Context; Ljava/lang/String; J)":
    "ACCESS_DOWNLOAD_MANAGER",
    "Landroid/net/Downloads$ByUri;-removeAllDownloadsByPackage-(Landroid/content/Context; Ljava/lang/String; Ljava/lang/String;)":
    "ACCESS_DOWNLOAD_MANAGER",
    "Landroid/net/Downloads$ByUri;-startDownloadByUri-(Landroid/content/Context; Ljava/lang/String; Ljava/lang/String; B I B B Ljava/lang/String; Ljava/lang/String; Ljava/lang/String; Ljava/lang/String;)":
    "ACCESS_DOWNLOAD_MANAGER",
    "Landroid/net/Downloads$ById;-deleteDownload-(Landroid/content/Context; J)":
    "ACCESS_DOWNLOAD_MANAGER",
    "Landroid/net/Downloads$ById;-getMimeTypeForId-(Landroid/content/Context; J)":
    "ACCESS_DOWNLOAD_MANAGER",
    "Landroid/net/Downloads$ById;-getStatus-(Landroid/content/Context; J)":
    "ACCESS_DOWNLOAD_MANAGER",
    "Landroid/net/Downloads$ById;-openDownload-(Landroid/content/Context; J Ljava/lang/String;)":
    "ACCESS_DOWNLOAD_MANAGER",
    "Landroid/net/Downloads$ById;-openDownloadStream-(Landroid/content/Context; J)":
    "ACCESS_DOWNLOAD_MANAGER",
    "Landroid/net/Downloads$ById;-startDownloadByUri-(Landroid/content/Context; Ljava/lang/String; Ljava/lang/String; B I B B Ljava/lang/String; Ljava/lang/String; Ljava/lang/String; Ljava/lang/String;)":
    "ACCESS_DOWNLOAD_MANAGER",
    "Landroid/view/IWindowManager$Stub$Proxy;-getDPadKeycodeState-(I)":
    "READ_INPUT_STATE",
    "Landroid/view/IWindowManager$Stub$Proxy;-getDPadScancodeState-(I)":
    "READ_INPUT_STATE",
    "Landroid/view/IWindowManager$Stub$Proxy;-getKeycodeState-(I)": "READ_INPUT_STATE",
    "Landroid/view/IWindowManager$Stub$Proxy;-getKeycodeStateForDevice-(I I)":
    "READ_INPUT_STATE",
    "Landroid/view/IWindowManager$Stub$Proxy;-getScancodeState-(I)": "READ_INPUT_STATE",
    "Landroid/view/IWindowManager$Stub$Proxy;-getScancodeStateForDevice-(I I)":
    "READ_INPUT_STATE",
    "Landroid/view/IWindowManager$Stub$Proxy;-getSwitchState-(I)": "READ_INPUT_STATE",
    "Landroid/view/IWindowManager$Stub$Proxy;-getSwitchStateForDevice-(I I)":
    "READ_INPUT_STATE",
    "Landroid/view/IWindowManager$Stub$Proxy;-getTrackballKeycodeState-(I)":
    "READ_INPUT_STATE",
    "Landroid/view/IWindowManager$Stub$Proxy;-getTrackballScancodeState-(I)":
    "READ_INPUT_STATE",
    "Landroid/app/ContextImpl$ApplicationContentResolver;-getCurrentSync-()":
    "READ_SYNC_STATS",
    "Landroid/app/ContextImpl$ApplicationContentResolver;-getSyncStatus-(Landroid/accounts/Account; Ljava/lang/String;)":
    "READ_SYNC_STATS",
    "Landroid/app/ContextImpl$ApplicationContentResolver;-isSyncActive-(Landroid/accounts/Account; Ljava/lang/String;)":
    "READ_SYNC_STATS",
    "Landroid/app/ContextImpl$ApplicationContentResolver;-isSyncPending-(Landroid/accounts/Account; Ljava/lang/String;)":
    "READ_SYNC_STATS",
    "Landroid/content/ContentService;-getCurrentSync-()": "READ_SYNC_STATS",
    "Landroid/content/ContentService;-getSyncStatus-(Landroid/accounts/Account; Ljava/lang/String;)":
    "READ_SYNC_STATS",
    "Landroid/content/ContentService;-isSyncActive-(Landroid/accounts/Account; Ljava/lang/String;)":
    "READ_SYNC_STATS",
    "Landroid/content/ContentService;-isSyncPending-(Landroid/accounts/Account; Ljava/lang/String;)":
    "READ_SYNC_STATS",
    "Landroid/content/ContentResolver;-getCurrentSync-()": "READ_SYNC_STATS",
    "Landroid/content/ContentResolver;-getSyncStatus-(Landroid/accounts/Account; Ljava/lang/String;)":
    "READ_SYNC_STATS",
    "Landroid/content/ContentResolver;-isSyncActive-(Landroid/accounts/Account; Ljava/lang/String;)":
    "READ_SYNC_STATS",
    "Landroid/content/ContentResolver;-isSyncPending-(Landroid/accounts/Account; Ljava/lang/String;)":
    "READ_SYNC_STATS",
    "Landroid/content/IContentService$Stub$Proxy;-getCurrentSync-()": "READ_SYNC_STATS",
    "Landroid/content/IContentService$Stub$Proxy;-getSyncStatus-(Landroid/accounts/Account; Ljava/lang/String;)":
    "READ_SYNC_STATS",
    "Landroid/content/IContentService$Stub$Proxy;-isSyncActive-(Landroid/accounts/Account; Ljava/lang/String;)":
    "READ_SYNC_STATS",
    "Landroid/content/IContentService$Stub$Proxy;-isSyncPending-(Landroid/accounts/Account; Ljava/lang/String;)":
    "READ_SYNC_STATS",
    "Landroid/app/AlarmManager;-setTime-(J)": "SET_TIME",
    "Landroid/app/AlarmManager;-setTimeZone-(Ljava/lang/String;)": "SET_TIME",
    "Landroid/app/AlarmManager;-setTime-(J)": "SET_TIME",
    "Landroid/app/IAlarmManager$Stub$Proxy;-setTime-(J)": "SET_TIME",
    "Lcom/htc/net/wimax/WimaxController$Stub$Proxy;-setWimaxEnable-()":
    "CHANGE_WIMAX_STATE",
    "Landroid/os/IMountService$Stub$Proxy;-mountMedi-()": "MOUNT_UNMOUNT_FILESYSTEMS",
    "Landroid/os/IMountService$Stub$Proxy;-unmountMedi-()": "MOUNT_UNMOUNT_FILESYSTEMS",
    "Landroid/os/storage/IMountService$Stub$Proxy;-getStorageUsers-(Ljava/lang/String;)":
    "MOUNT_UNMOUNT_FILESYSTEMS",
    "Landroid/os/storage/IMountService$Stub$Proxy;-mountVolume-(Ljava/lang/String;)":
    "MOUNT_UNMOUNT_FILESYSTEMS",
    "Landroid/os/storage/IMountService$Stub$Proxy;-setUsbMassStorageEnabled-(B)":
    "MOUNT_UNMOUNT_FILESYSTEMS",
    "Landroid/os/storage/IMountService$Stub$Proxy;-unmountVolume-(Ljava/lang/String; B)":
    "MOUNT_UNMOUNT_FILESYSTEMS",
    "Landroid/os/storage/StorageManager;-disableUsbMassStorage-()":
    "MOUNT_UNMOUNT_FILESYSTEMS",
    "Landroid/os/storage/StorageManager;-enableUsbMassStorage-()":
    "MOUNT_UNMOUNT_FILESYSTEMS",
    "Landroid/app/ContextImpl$ApplicationPackageManager;-movePackage-(Ljava/lang/String; LIPackageMoveObserver; I)":
    "MOVE_PACKAGE",
    "Landroid/app/ContextImpl$ApplicationPackageManager;-movePackage-(Ljava/lang/String; LIPackageMoveObserver; I)":
    "MOVE_PACKAGE",
    "Landroid/content/pm/PackageManager;-movePackage-(Ljava/lang/String; LIPackageMoveObserver; I)":
    "MOVE_PACKAGE",
    "Landroid/content/pm/IPackageManager$Stub$Proxy;-movePackage-(Ljava/lang/String; Landroid/content/pm/IPackageMoveObserver; I)":
    "MOVE_PACKAGE",
    "Lcom/htc/net/wimax/WimaxController$Stub$Proxy;-getConnectionInf-()":
    "ACCESS_WIMAX_STATE",
    "Lcom/htc/net/wimax/WimaxController$Stub$Proxy;-getWimaxStat-()": "ACCESS_WIMAX_STATE",
    "Lcom/htc/net/wimax/WimaxController$Stub$Proxy;-isBackoffStat-()":
    "ACCESS_WIMAX_STATE",
    "Lcom/htc/net/wimax/WimaxController$Stub$Proxy;-isWimaxEnable-()":
    "ACCESS_WIMAX_STATE",
    "Landroid/net/sip/SipAudioCall;-startAudio-()": "ACCESS_WIFI_STATE",
    "Landroid/net/wifi/IWifiManager$Stub$Proxy;-getConfiguredNetworks-()":
    "ACCESS_WIFI_STATE",
    "Landroid/net/wifi/IWifiManager$Stub$Proxy;-getConnectionInfo-()": "ACCESS_WIFI_STATE",
    "Landroid/net/wifi/IWifiManager$Stub$Proxy;-getDhcpInfo-()": "ACCESS_WIFI_STATE",
    "Landroid/net/wifi/IWifiManager$Stub$Proxy;-getNumAllowedChannels-()":
    "ACCESS_WIFI_STATE",
    "Landroid/net/wifi/IWifiManager$Stub$Proxy;-getScanResults-()": "ACCESS_WIFI_STATE",
    "Landroid/net/wifi/IWifiManager$Stub$Proxy;-getValidChannelCounts-()":
    "ACCESS_WIFI_STATE",
    "Landroid/net/wifi/IWifiManager$Stub$Proxy;-getWifiApEnabledState-()":
    "ACCESS_WIFI_STATE",
    "Landroid/net/wifi/IWifiManager$Stub$Proxy;-getWifiEnabledState-()":
    "ACCESS_WIFI_STATE",
    "Landroid/net/wifi/IWifiManager$Stub$Proxy;-isMulticastEnabled-()":
    "ACCESS_WIFI_STATE",
    "Landroid/net/wifi/WifiManager;-getConfiguredNetworks-()": "ACCESS_WIFI_STATE",
    "Landroid/net/wifi/WifiManager;-getConnectionInfo-()": "ACCESS_WIFI_STATE",
    "Landroid/net/wifi/WifiManager;-getDhcpInfo-()": "ACCESS_WIFI_STATE",
    "Landroid/net/wifi/WifiManager;-getNumAllowedChannels-()": "ACCESS_WIFI_STATE",
    "Landroid/net/wifi/WifiManager;-getScanResults-()": "ACCESS_WIFI_STATE",
    "Landroid/net/wifi/WifiManager;-getValidChannelCounts-()": "ACCESS_WIFI_STATE",
    "Landroid/net/wifi/WifiManager;-getWifiApState-()": "ACCESS_WIFI_STATE",
    "Landroid/net/wifi/WifiManager;-getWifiState-()": "ACCESS_WIFI_STATE",
    "Landroid/net/wifi/WifiManager;-isMulticastEnabled-()": "ACCESS_WIFI_STATE",
    "Landroid/net/wifi/WifiManager;-isWifiApEnabled-()": "ACCESS_WIFI_STATE",
    "Landroid/net/wifi/WifiManager;-isWifiEnabled-()": "ACCESS_WIFI_STATE",
    "Landroid/webkit/WebIconDatabase;-bulkRequestIconForPageUrl-(Landroid/content/ContentResolver; Ljava/lang/String; Landroid/webkit/WebIconDatabase$IconListener;)":
    "READ_HISTORY_BOOKMARKS",
    "Landroid/provider/Browser;-BOOKMARKS_URI-Landroid/net/Uri;": "READ_HISTORY_BOOKMARKS",
    "Landroid/provider/Browser;-SEARCHES_URI-Landroid/net/Uri;": "READ_HISTORY_BOOKMARKS",
    "Landroid/provider/Browser;-addSearchUrl-(Landroid/content/ContentResolver; Ljava/lang/String;)":
    "READ_HISTORY_BOOKMARKS",
    "Landroid/provider/Browser;-canClearHistory-(Landroid/content/ContentResolver;)":
    "READ_HISTORY_BOOKMARKS",
    "Landroid/provider/Browser;-getAllBookmarks-(Landroid/content/ContentResolver;)":
    "READ_HISTORY_BOOKMARKS",
    "Landroid/provider/Browser;-getAllVisitedUrls-(Landroid/content/ContentResolver;)":
    "READ_HISTORY_BOOKMARKS",
    "Landroid/provider/Browser;-requestAllIcons-(Landroid/content/ContentResolver; Ljava/lang/String; Landroid/webkit/WebIconDatabase/IconListener;)":
    "READ_HISTORY_BOOKMARKS",
    "Landroid/provider/Browser;-truncateHistory-(Landroid/content/ContentResolver;)":
    "READ_HISTORY_BOOKMARKS",
    "Landroid/provider/Browser;-updateVisitedHistory-(Landroid/content/ContentResolver; Ljava/lang/String; B)":
    "READ_HISTORY_BOOKMARKS",
    "Landroid/provider/Browser;-addSearchUrl-(Landroid/content/ContentResolver; Ljava/lang/String;)":
    "READ_HISTORY_BOOKMARKS",
    "Landroid/provider/Browser;-canClearHistory-(Landroid/content/ContentResolver;)":
    "READ_HISTORY_BOOKMARKS",
    "Landroid/provider/Browser;-clearHistory-(Landroid/content/ContentResolver;)":
    "READ_HISTORY_BOOKMARKS",
    "Landroid/provider/Browser;-deleteFromHistory-(Landroid/content/ContentResolver; Ljava/lang/String;)":
    "READ_HISTORY_BOOKMARKS",
    "Landroid/provider/Browser;-deleteHistoryTimeFrame-(Landroid/content/ContentResolver; J J)":
    "READ_HISTORY_BOOKMARKS",
    "Landroid/provider/Browser;-deleteHistoryWhere-(Landroid/content/ContentResolver; Ljava/lang/String;)":
    "READ_HISTORY_BOOKMARKS",
    "Landroid/provider/Browser;-getAllBookmarks-(Landroid/content/ContentResolver;)":
    "READ_HISTORY_BOOKMARKS",
    "Landroid/provider/Browser;-getAllVisitedUrls-(Landroid/content/ContentResolver;)":
    "READ_HISTORY_BOOKMARKS",
    "Landroid/provider/Browser;-getVisitedHistory-(Landroid/content/ContentResolver;)":
    "READ_HISTORY_BOOKMARKS",
    "Landroid/provider/Browser;-getVisitedLike-(Landroid/content/ContentResolver; Ljava/lang/String;)":
    "READ_HISTORY_BOOKMARKS",
    "Landroid/provider/Browser;-requestAllIcons-(Landroid/content/ContentResolver; Ljava/lang/String; Landroid/webkit/WebIconDatabase$IconListener;)":
    "READ_HISTORY_BOOKMARKS",
    "Landroid/provider/Browser;-truncateHistory-(Landroid/content/ContentResolver;)":
    "READ_HISTORY_BOOKMARKS",
    "Landroid/provider/Browser;-updateVisitedHistory-(Landroid/content/ContentResolver; Ljava/lang/String; B)":
    "READ_HISTORY_BOOKMARKS",
    "Landroid/os/storage/IMountService$Stub$Proxy;-destroySecureContainer-(Ljava/lang/String; B)":
    "ASEC_DESTROY",
    "Landroid/net/ThrottleManager;-getByteCount-(Ljava/lang/String; I I I)":
    "ACCESS_NETWORK_STATE",
    "Landroid/net/ThrottleManager;-getCliffLevel-(Ljava/lang/String; I)":
    "ACCESS_NETWORK_STATE",
    "Landroid/net/ThrottleManager;-getCliffThreshold-(Ljava/lang/String; I)":
    "ACCESS_NETWORK_STATE",
    "Landroid/net/ThrottleManager;-getHelpUri-()": "ACCESS_NETWORK_STATE",
    "Landroid/net/ThrottleManager;-getPeriodStartTime-(Ljava/lang/String;)":
    "ACCESS_NETWORK_STATE",
    "Landroid/net/ThrottleManager;-getResetTime-(Ljava/lang/String;)":
    "ACCESS_NETWORK_STATE",
    "Landroid/net/NetworkInfo;-isConnectedOrConnecting-()": "ACCESS_NETWORK_STATE",
    "Landroid/os/INetworkManagementService$Stub$Proxy;-getDnsForwarders-()":
    "ACCESS_NETWORK_STATE",
    "Landroid/os/INetworkManagementService$Stub$Proxy;-getInterfaceRxCounter-(Ljava/lang/String;)":
    "ACCESS_NETWORK_STATE",
    "Landroid/os/INetworkManagementService$Stub$Proxy;-getInterfaceRxThrottle-(Ljava/lang/String;)":
    "ACCESS_NETWORK_STATE",
    "Landroid/os/INetworkManagementService$Stub$Proxy;-getInterfaceTxCounter-(Ljava/lang/String;)":
    "ACCESS_NETWORK_STATE",
    "Landroid/os/INetworkManagementService$Stub$Proxy;-getInterfaceTxThrottle-(Ljava/lang/String;)":
    "ACCESS_NETWORK_STATE",
    "Landroid/os/INetworkManagementService$Stub$Proxy;-getIpForwardingEnabled-()":
    "ACCESS_NETWORK_STATE",
    "Landroid/os/INetworkManagementService$Stub$Proxy;-isTetheringStarted-()":
    "ACCESS_NETWORK_STATE",
    "Landroid/os/INetworkManagementService$Stub$Proxy;-isUsbRNDISStarted-()":
    "ACCESS_NETWORK_STATE",
    "Landroid/os/INetworkManagementService$Stub$Proxy;-listInterfaces-()":
    "ACCESS_NETWORK_STATE",
    "Landroid/os/INetworkManagementService$Stub$Proxy;-listTetheredInterfaces-()":
    "ACCESS_NETWORK_STATE",
    "Landroid/os/INetworkManagementService$Stub$Proxy;-listTtys-()":
    "ACCESS_NETWORK_STATE",
    "Landroid/net/IConnectivityManager$Stub$Proxy;-getActiveNetworkInfo-()":
    "ACCESS_NETWORK_STATE",
    "Landroid/net/IConnectivityManager$Stub$Proxy;-getAllNetworkInfo-()":
    "ACCESS_NETWORK_STATE",
    "Landroid/net/IConnectivityManager$Stub$Proxy;-getLastTetherError-(Ljava/lang/String;)":
    "ACCESS_NETWORK_STATE",
    "Landroid/net/IConnectivityManager$Stub$Proxy;-getMobileDataEnabled-()":
    "ACCESS_NETWORK_STATE",
    "Landroid/net/IConnectivityManager$Stub$Proxy;-getNetworkInfo-(I)":
    "ACCESS_NETWORK_STATE",
    "Landroid/net/IConnectivityManager$Stub$Proxy;-getNetworkPreference-()":
    "ACCESS_NETWORK_STATE",
    "Landroid/net/IConnectivityManager$Stub$Proxy;-getTetherableIfaces-()":
    "ACCESS_NETWORK_STATE",
    "Landroid/net/IConnectivityManager$Stub$Proxy;-getTetherableUsbRegexs-()":
    "ACCESS_NETWORK_STATE",
    "Landroid/net/IConnectivityManager$Stub$Proxy;-getTetherableWifiRegexs-()":
    "ACCESS_NETWORK_STATE",
    "Landroid/net/IConnectivityManager$Stub$Proxy;-getTetheredIfaces-()":
    "ACCESS_NETWORK_STATE",
    "Landroid/net/IConnectivityManager$Stub$Proxy;-getTetheringErroredIfaces-()":
    "ACCESS_NETWORK_STATE",
    "Landroid/net/IConnectivityManager$Stub$Proxy;-isTetheringSupported-()":
    "ACCESS_NETWORK_STATE",
    "Landroid/net/IConnectivityManager$Stub$Proxy;-startUsingNetworkFeature-(I Ljava/lang/String; Landroid/os/IBinder;)":
    "ACCESS_NETWORK_STATE",
    "Landroid/net/IThrottleManager$Stub$Proxy;-getByteCount-(Ljava/lang/String; I I I)":
    "ACCESS_NETWORK_STATE",
    "Landroid/net/IThrottleManager$Stub$Proxy;-getCliffLevel-(Ljava/lang/String; I)":
    "ACCESS_NETWORK_STATE",
    "Landroid/net/IThrottleManager$Stub$Proxy;-getCliffThreshold-(Ljava/lang/String; I)":
    "ACCESS_NETWORK_STATE",
    "Landroid/net/IThrottleManager$Stub$Proxy;-getHelpUri-()": "ACCESS_NETWORK_STATE",
    "Landroid/net/IThrottleManager$Stub$Proxy;-getPeriodStartTime-(Ljava/lang/String;)":
    "ACCESS_NETWORK_STATE",
    "Landroid/net/IThrottleManager$Stub$Proxy;-getResetTime-(Ljava/lang/String;)":
    "ACCESS_NETWORK_STATE",
    "Landroid/net/IThrottleManager$Stub$Proxy;-getThrottle-(Ljava/lang/String;)":
    "ACCESS_NETWORK_STATE",
    "Landroid/net/ConnectivityManager;-getActiveNetworkInfo-()": "ACCESS_NETWORK_STATE",
    "Landroid/net/ConnectivityManager;-getAllNetworkInfo-()": "ACCESS_NETWORK_STATE",
    "Landroid/net/ConnectivityManager;-getLastTetherError-(Ljava/lang/String;)":
    "ACCESS_NETWORK_STATE",
    "Landroid/net/ConnectivityManager;-getMobileDataEnabled-()": "ACCESS_NETWORK_STATE",
    "Landroid/net/ConnectivityManager;-getNetworkInfo-(I)": "ACCESS_NETWORK_STATE",
    "Landroid/net/ConnectivityManager;-getNetworkPreference-()": "ACCESS_NETWORK_STATE",
    "Landroid/net/ConnectivityManager;-getTetherableIfaces-()": "ACCESS_NETWORK_STATE",
    "Landroid/net/ConnectivityManager;-getTetherableUsbRegexs-()": "ACCESS_NETWORK_STATE",
    "Landroid/net/ConnectivityManager;-getTetherableWifiRegexs-()": "ACCESS_NETWORK_STATE",
    "Landroid/net/ConnectivityManager;-getTetheredIfaces-()": "ACCESS_NETWORK_STATE",
    "Landroid/net/ConnectivityManager;-getTetheringErroredIfaces-()":
    "ACCESS_NETWORK_STATE",
    "Landroid/net/ConnectivityManager;-isTetheringSupported-()": "ACCESS_NETWORK_STATE",
    "Landroid/net/http/RequestQueue;-enablePlatformNotifications-()":
    "ACCESS_NETWORK_STATE",
    "Landroid/net/http/RequestQueue;-setProxyConfig-()": "ACCESS_NETWORK_STATE",
    "Landroid/app/IActivityManager$Stub$Proxy;-getRecentTasks-(I I)": "GET_TASKS",
    "Landroid/app/IActivityManager$Stub$Proxy;-getTasks-(I I Landroid/app/IThumbnailReceiver;)":
    "GET_TASKS",
    "Landroid/app/ActivityManagerNative;-getRecentTasks-(I I)": "GET_TASKS",
    "Landroid/app/ActivityManagerNative;-getRunningTasks-(I)": "GET_TASKS",
    "Landroid/app/ActivityManager;-getRecentTasks-(I I)": "GET_TASKS",
    "Landroid/app/ActivityManager;-getRunningTasks-(I)": "GET_TASKS",
    "Landroid/app/ActivityManager;-getRecentTasks-(I I)": "GET_TASKS",
    "Landroid/app/ActivityManager;-getRunningTasks-(I)": "GET_TASKS",
    "Landroid/view/View/OnSystemUiVisibilityChangeListener;-onSystemUiVisibilityChange-(I)":
    "STATUS_BAR",
    "Landroid/view/View;-STATUS_BAR_HIDDEN-I": "STATUS_BAR",
    "Landroid/view/View;-STATUS_BAR_VISIBLE-I": "STATUS_BAR",
    "Landroid/app/StatusBarManager;-addIcon-(Ljava/lang/String; I I)": "STATUS_BAR",
    "Landroid/app/StatusBarManager;-disable-(I)": "STATUS_BAR",
    "Landroid/app/StatusBarManager;-removeIcon-(Landroid/os/IBinder;)": "STATUS_BAR",
    "Landroid/app/StatusBarManager;-updateIcon-(Landroid/os/IBinder; Ljava/lang/String; I I)":
    "STATUS_BAR",
    "Landroid/view/WindowManager/LayoutParams;-TYPE_STATUS_BAR-I": "STATUS_BAR",
    "Landroid/view/WindowManager/LayoutParams;-TYPE_STATUS_BAR_PANEL-I": "STATUS_BAR",
    "Landroid/view/WindowManager/LayoutParams;-systemUiVisibility-I": "STATUS_BAR",
    "Landroid/view/WindowManager/LayoutParams;-type-I": "STATUS_BAR",
    "Landroid/app/IStatusBar$Stub$Proxy;-addIcon-(Ljava/lang/String; Ljava/lang/String; I I)":
    "STATUS_BAR",
    "Landroid/app/IStatusBar$Stub$Proxy;-disable-(I Landroid/os/IBinder; Ljava/lang/String;)":
    "STATUS_BAR",
    "Landroid/app/IStatusBar$Stub$Proxy;-removeIcon-(Landroid/os/IBinder;)": "STATUS_BAR",
    "Landroid/app/IStatusBar$Stub$Proxy;-updateIcon-(Landroid/os/IBinder; Ljava/lang/String; Ljava/lang/String; I I)":
    "STATUS_BAR",
    "Landroid/app/IActivityManager$Stub$Proxy;-shutdown-(I)": "SHUTDOWN",
    "Landroid/os/IMountService$Stub$Proxy;-shutdow-()": "SHUTDOWN",
    "Landroid/os/storage/IMountService$Stub$Proxy;-shutdown-(Landroid/os/storage/IMountShutdownObserver;)":
    "SHUTDOWN",
    "Landroid/os/INetworkManagementService$Stub$Proxy;-shutdown-()": "SHUTDOWN",
    "Landroid/os/DropBoxManager;-ACTION_DROPBOX_ENTRY_ADDED-Ljava/lang/String;":
    "READ_LOGS",
    "Landroid/os/DropBoxManager;-getNextEntry-(Ljava/lang/String; J)": "READ_LOGS",
    "Landroid/os/DropBoxManager;-getNextEntry-(Ljava/lang/String; J)": "READ_LOGS",
    "Lcom/android/internal/os/IDropBoxManagerService$Stub$Proxy;-getNextEntry-(Ljava/lang/String; J)":
    "READ_LOGS",
    "Ljava/lang/Runtime;-exec-(Ljava/lang/String;)": "READ_LOGS",
    "Ljava/lang/Runtime;-exec-([Ljava/lang/String;)": "READ_LOGS",
    "Ljava/lang/Runtime;-exec-([Ljava/lang/String; [Ljava/lang/String;)": "READ_LOGS",
    "Ljava/lang/Runtime;-exec-([Ljava/lang/String; [Ljava/lang/String; Ljava/io/File;)":
    "READ_LOGS",
    "Ljava/lang/Runtime;-exec-(Ljava/lang/String; [Ljava/lang/String;)": "READ_LOGS",
    "Ljava/lang/Runtime;-exec-(Ljava/lang/String; [Ljava/lang/String; Ljava/io/File;)":
    "READ_LOGS",
    "Landroid/os/Process;-BLUETOOTH_GID-I": "BLUETOOTH",
    "Landroid/bluetooth/BluetoothA2dp;-ACTION_CONNECTION_STATE_CHANGED-Ljava/lang/String;":
    "BLUETOOTH",
    "Landroid/bluetooth/BluetoothA2dp;-ACTION_PLAYING_STATE_CHANGED-Ljava/lang/String;":
    "BLUETOOTH",
    "Landroid/bluetooth/BluetoothA2dp;-getConnectedDevices-()": "BLUETOOTH",
    "Landroid/bluetooth/BluetoothA2dp;-getConnectionState-(Landroid/bluetooth/BluetoothDevice;)":
    "BLUETOOTH",
    "Landroid/bluetooth/BluetoothA2dp;-getDevicesMatchingConnectionStates-([I)":
    "BLUETOOTH",
    "Landroid/bluetooth/BluetoothA2dp;-isA2dpPlaying-(Landroid/bluetooth/BluetoothDevice;)":
    "BLUETOOTH",
    "Landroid/bluetooth/BluetoothA2dp;-getConnectedSinks-()": "BLUETOOTH",
    "Landroid/bluetooth/BluetoothA2dp;-getNonDisconnectedSinks-()": "BLUETOOTH",
    "Landroid/bluetooth/BluetoothA2dp;-getSinkPriority-(Landroid/bluetooth/BluetoothDevice;)":
    "BLUETOOTH",
    "Landroid/bluetooth/BluetoothA2dp;-getSinkState-(Landroid/bluetooth/BluetoothDevice;)":
    "BLUETOOTH",
    "Landroid/bluetooth/BluetoothA2dp;-isSinkConnected-(Landroid/bluetooth/BluetoothDevice;)":
    "BLUETOOTH",
    "Landroid/media/AudioManager;-ROUTE_BLUETOOTH-I": "BLUETOOTH",
    "Landroid/media/AudioManager;-ROUTE_BLUETOOTH_A2DP-I": "BLUETOOTH",
    "Landroid/media/AudioManager;-ROUTE_BLUETOOTH_SCO-I": "BLUETOOTH",
    "Landroid/bluetooth/IBluetoothA2dp$Stub$Proxy;-getConnectedSinks-()": "BLUETOOTH",
    "Landroid/bluetooth/IBluetoothA2dp$Stub$Proxy;-getNonDisconnectedSinks-()": "BLUETOOTH",
    "Landroid/bluetooth/IBluetoothA2dp$Stub$Proxy;-getSinkPriority-(Landroid/bluetooth/BluetoothDevice;)":
    "BLUETOOTH",
    "Landroid/bluetooth/IBluetoothA2dp$Stub$Proxy;-getSinkState-(Landroid/bluetooth/BluetoothDevice;)":
    "BLUETOOTH",
    "Landroid/bluetooth/BluetoothSocket;-connect-()": "BLUETOOTH",
    "Landroid/bluetooth/BluetoothPbap;-getClient-()": "BLUETOOTH",
    "Landroid/bluetooth/BluetoothPbap;-getState-()": "BLUETOOTH",
    "Landroid/bluetooth/BluetoothPbap;-isConnected-(Landroid/bluetooth/BluetoothDevice;)":
    "BLUETOOTH",
    "Landroid/provider/Settings/System;-AIRPLANE_MODE_RADIOS-Ljava/lang/String;":
    "BLUETOOTH",
    "Landroid/provider/Settings/System;-BLUETOOTH_DISCOVERABILITY-Ljava/lang/String;":
    "BLUETOOTH",
    "Landroid/provider/Settings/System;-BLUETOOTH_DISCOVERABILITY_TIMEOUT-Ljava/lang/String;":
    "BLUETOOTH",
    "Landroid/provider/Settings/System;-BLUETOOTH_ON-Ljava/lang/String;": "BLUETOOTH",
    "Landroid/provider/Settings/System;-RADIO_BLUETOOTH-Ljava/lang/String;": "BLUETOOTH",
    "Landroid/provider/Settings/System;-VOLUME_BLUETOOTH_SCO-Ljava/lang/String;":
    "BLUETOOTH",
    "Landroid/provider/Settings;-ACTION_BLUETOOTH_SETTINGS-Ljava/lang/String;": "BLUETOOTH",
    "Landroid/bluetooth/IBluetooth$Stub$Proxy;-addRfcommServiceRecord-(Ljava/lang/String; Landroid/os/ParcelUuid; I Landroid/os/IBinder;)":
    "BLUETOOTH",
    "Landroid/bluetooth/IBluetooth$Stub$Proxy;-fetchRemoteUuids-(Ljava/lang/String; Landroid/os/ParcelUuid; Landroid/bluetooth/IBluetoothCallback;)":
    "BLUETOOTH",
    "Landroid/bluetooth/IBluetooth$Stub$Proxy;-getAddress-()": "BLUETOOTH",
    "Landroid/bluetooth/IBluetooth$Stub$Proxy;-getBluetoothState-()": "BLUETOOTH",
    "Landroid/bluetooth/IBluetooth$Stub$Proxy;-getBondState-(Ljava/lang/String;)":
    "BLUETOOTH",
    "Landroid/bluetooth/IBluetooth$Stub$Proxy;-getDiscoverableTimeout-()": "BLUETOOTH",
    "Landroid/bluetooth/IBluetooth$Stub$Proxy;-getName-()": "BLUETOOTH",
    "Landroid/bluetooth/IBluetooth$Stub$Proxy;-getRemoteClass-(Ljava/lang/String;)":
    "BLUETOOTH",
    "Landroid/bluetooth/IBluetooth$Stub$Proxy;-getRemoteName-(Ljava/lang/String;)":
    "BLUETOOTH",
    "Landroid/bluetooth/IBluetooth$Stub$Proxy;-getRemoteServiceChannel-(Ljava/lang/String; Landroid/os/ParcelUuid;)":
    "BLUETOOTH",
    "Landroid/bluetooth/IBluetooth$Stub$Proxy;-getRemoteUuids-(Ljava/lang/String;)":
    "BLUETOOTH",
    "Landroid/bluetooth/IBluetooth$Stub$Proxy;-getScanMode-()": "BLUETOOTH",
    "Landroid/bluetooth/IBluetooth$Stub$Proxy;-getTrustState-(Ljava/lang/String;)":
    "BLUETOOTH",
    "Landroid/bluetooth/IBluetooth$Stub$Proxy;-isDiscovering-()": "BLUETOOTH",
    "Landroid/bluetooth/IBluetooth$Stub$Proxy;-isEnabled-()": "BLUETOOTH",
    "Landroid/bluetooth/IBluetooth$Stub$Proxy;-listBonds-()": "BLUETOOTH",
    "Landroid/bluetooth/IBluetooth$Stub$Proxy;-removeServiceRecord-(I)": "BLUETOOTH",
    "Landroid/bluetooth/BluetoothAdapter;-ACTION_CONNECTION_STATE_CHANGED-Ljava/lang/String;":
    "BLUETOOTH",
    "Landroid/bluetooth/BluetoothAdapter;-ACTION_DISCOVERY_FINISHED-Ljava/lang/String;":
    "BLUETOOTH",
    "Landroid/bluetooth/BluetoothAdapter;-ACTION_DISCOVERY_STARTED-Ljava/lang/String;":
    "BLUETOOTH",
    "Landroid/bluetooth/BluetoothAdapter;-ACTION_LOCAL_NAME_CHANGED-Ljava/lang/String;":
    "BLUETOOTH",
    "Landroid/bluetooth/BluetoothAdapter;-ACTION_REQUEST_DISCOVERABLE-Ljava/lang/String;":
    "BLUETOOTH",
    "Landroid/bluetooth/BluetoothAdapter;-ACTION_REQUEST_ENABLE-Ljava/lang/String;":
    "BLUETOOTH",
    "Landroid/bluetooth/BluetoothAdapter;-ACTION_SCAN_MODE_CHANGED-Ljava/lang/String;":
    "BLUETOOTH",
    "Landroid/bluetooth/BluetoothAdapter;-ACTION_STATE_CHANGED-Ljava/lang/String;":
    "BLUETOOTH",
    "Landroid/bluetooth/BluetoothAdapter;-cancelDiscovery-()": "BLUETOOTH",
    "Landroid/bluetooth/BluetoothAdapter;-disable-()": "BLUETOOTH",
    "Landroid/bluetooth/BluetoothAdapter;-enable-()": "BLUETOOTH",
    "Landroid/bluetooth/BluetoothAdapter;-getAddress-()": "BLUETOOTH",
    "Landroid/bluetooth/BluetoothAdapter;-getBondedDevices-()": "BLUETOOTH",
    "Landroid/bluetooth/BluetoothAdapter;-getName-()": "BLUETOOTH",
    "Landroid/bluetooth/BluetoothAdapter;-getScanMode-()": "BLUETOOTH",
    "Landroid/bluetooth/BluetoothAdapter;-getState-()": "BLUETOOTH",
    "Landroid/bluetooth/BluetoothAdapter;-isDiscovering-()": "BLUETOOTH",
    "Landroid/bluetooth/BluetoothAdapter;-isEnabled-()": "BLUETOOTH",
    "Landroid/bluetooth/BluetoothAdapter;-listenUsingInsecureRfcommWithServiceRecord-(Ljava/lang/String; Ljava/util/UUID;)":
    "BLUETOOTH",
    "Landroid/bluetooth/BluetoothAdapter;-listenUsingRfcommWithServiceRecord-(Ljava/lang/String; Ljava/util/UUID;)":
    "BLUETOOTH",
    "Landroid/bluetooth/BluetoothAdapter;-setName-(Ljava/lang/String;)": "BLUETOOTH",
    "Landroid/bluetooth/BluetoothAdapter;-startDiscovery-()": "BLUETOOTH",
    "Landroid/bluetooth/BluetoothAdapter;-getAddress-()": "BLUETOOTH",
    "Landroid/bluetooth/BluetoothAdapter;-getBondedDevices-()": "BLUETOOTH",
    "Landroid/bluetooth/BluetoothAdapter;-getDiscoverableTimeout-()": "BLUETOOTH",
    "Landroid/bluetooth/BluetoothAdapter;-getName-()": "BLUETOOTH",
    "Landroid/bluetooth/BluetoothAdapter;-getScanMode-()": "BLUETOOTH",
    "Landroid/bluetooth/BluetoothAdapter;-getState-()": "BLUETOOTH",
    "Landroid/bluetooth/BluetoothAdapter;-isDiscovering-()": "BLUETOOTH",
    "Landroid/bluetooth/BluetoothAdapter;-isEnabled-()": "BLUETOOTH",
    "Landroid/bluetooth/BluetoothAdapter;-listenUsingRfcommWithServiceRecord-(Ljava/lang/String; Ljava/util/UUID;)":
    "BLUETOOTH",
    "Landroid/bluetooth/BluetoothProfile;-getConnectedDevices-()": "BLUETOOTH",
    "Landroid/bluetooth/BluetoothProfile;-getConnectionState-(Landroid/bluetooth/BluetoothDevice;)":
    "BLUETOOTH",
    "Landroid/bluetooth/BluetoothProfile;-getDevicesMatchingConnectionStates-([I)":
    "BLUETOOTH",
    "Landroid/bluetooth/BluetoothHeadset;-ACTION_AUDIO_STATE_CHANGED-Ljava/lang/String;":
    "BLUETOOTH",
    "Landroid/bluetooth/BluetoothHeadset;-ACTION_CONNECTION_STATE_CHANGED-Ljava/lang/String;":
    "BLUETOOTH",
    "Landroid/bluetooth/BluetoothHeadset;-ACTION_VENDOR_SPECIFIC_HEADSET_EVENT-Ljava/lang/String;":
    "BLUETOOTH",
    "Landroid/bluetooth/BluetoothHeadset;-getConnectedDevices-()": "BLUETOOTH",
    "Landroid/bluetooth/BluetoothHeadset;-getConnectionState-(Landroid/bluetooth/BluetoothDevice;)":
    "BLUETOOTH",
    "Landroid/bluetooth/BluetoothHeadset;-getDevicesMatchingConnectionStates-([I)":
    "BLUETOOTH",
    "Landroid/bluetooth/BluetoothHeadset;-isAudioConnected-(Landroid/bluetooth/BluetoothDevice;)":
    "BLUETOOTH",
    "Landroid/bluetooth/BluetoothHeadset;-startVoiceRecognition-(Landroid/bluetooth/BluetoothDevice;)":
    "BLUETOOTH",
    "Landroid/bluetooth/BluetoothHeadset;-stopVoiceRecognition-(Landroid/bluetooth/BluetoothDevice;)":
    "BLUETOOTH",
    "Landroid/bluetooth/BluetoothHeadset;-getBatteryUsageHint-()": "BLUETOOTH",
    "Landroid/bluetooth/BluetoothHeadset;-getCurrentHeadset-()": "BLUETOOTH",
    "Landroid/bluetooth/BluetoothHeadset;-getPriority-(Landroid/bluetooth/BluetoothDevice;)":
    "BLUETOOTH",
    "Landroid/bluetooth/BluetoothHeadset;-getState-()": "BLUETOOTH",
    "Landroid/bluetooth/BluetoothHeadset;-isConnected-(Landroid/bluetooth/BluetoothDevice;)":
    "BLUETOOTH",
    "Landroid/bluetooth/BluetoothHeadset;-startVoiceRecognition-()": "BLUETOOTH",
    "Landroid/bluetooth/BluetoothHeadset;-stopVoiceRecognition-()": "BLUETOOTH",
    "Landroid/bluetooth/IBluetoothHeadset$Stub$Proxy;-getBatteryUsageHint-()": "BLUETOOTH",
    "Landroid/bluetooth/IBluetoothHeadset$Stub$Proxy;-getCurrentHeadset-()": "BLUETOOTH",
    "Landroid/bluetooth/IBluetoothHeadset$Stub$Proxy;-getPriority-(Landroid/bluetooth/BluetoothDevice;)":
    "BLUETOOTH",
    "Landroid/bluetooth/IBluetoothHeadset$Stub$Proxy;-getState-()": "BLUETOOTH",
    "Landroid/bluetooth/IBluetoothHeadset$Stub$Proxy;-isConnected-(Landroid/bluetooth/BluetoothDevice;)":
    "BLUETOOTH",
    "Landroid/bluetooth/IBluetoothHeadset$Stub$Proxy;-startVoiceRecognition-()": "BLUETOOTH",
    "Landroid/bluetooth/IBluetoothHeadset$Stub$Proxy;-stopVoiceRecognition-()": "BLUETOOTH",
    "Landroid/bluetooth/BluetoothDevice;-ACTION_ACL_CONNECTED-Ljava/lang/String;":
    "BLUETOOTH",
    "Landroid/bluetooth/BluetoothDevice;-ACTION_ACL_DISCONNECTED-Ljava/lang/String;":
    "BLUETOOTH",
    "Landroid/bluetooth/BluetoothDevice;-ACTION_ACL_DISCONNECT_REQUESTED-Ljava/lang/String;":
    "BLUETOOTH",
    "Landroid/bluetooth/BluetoothDevice;-ACTION_BOND_STATE_CHANGED-Ljava/lang/String;":
    "BLUETOOTH",
    "Landroid/bluetooth/BluetoothDevice;-ACTION_CLASS_CHANGED-Ljava/lang/String;":
    "BLUETOOTH",
    "Landroid/bluetooth/BluetoothDevice;-ACTION_FOUND-Ljava/lang/String;": "BLUETOOTH",
    "Landroid/bluetooth/BluetoothDevice;-ACTION_NAME_CHANGED-Ljava/lang/String;":
    "BLUETOOTH",
    "Landroid/bluetooth/BluetoothDevice;-createInsecureRfcommSocketToServiceRecord-(Ljava/util/UUID;)":
    "BLUETOOTH",
    "Landroid/bluetooth/BluetoothDevice;-createRfcommSocketToServiceRecord-(Ljava/util/UUID;)":
    "BLUETOOTH",
    "Landroid/bluetooth/BluetoothDevice;-getBluetoothClass-()": "BLUETOOTH",
    "Landroid/bluetooth/BluetoothDevice;-getBondState-()": "BLUETOOTH",
    "Landroid/bluetooth/BluetoothDevice;-getName-()": "BLUETOOTH",
    "Landroid/bluetooth/BluetoothDevice;-createRfcommSocketToServiceRecord-(Ljava/util/UUID;)":
    "BLUETOOTH",
    "Landroid/bluetooth/BluetoothDevice;-fetchUuidsWithSdp-()": "BLUETOOTH",
    "Landroid/bluetooth/BluetoothDevice;-getBondState-()": "BLUETOOTH",
    "Landroid/bluetooth/BluetoothDevice;-getName-()": "BLUETOOTH",
    "Landroid/bluetooth/BluetoothDevice;-getServiceChannel-(Landroid/os/ParcelUuid;)":
    "BLUETOOTH",
    "Landroid/bluetooth/BluetoothDevice;-getUuids-()": "BLUETOOTH",
    "Landroid/server/BluetoothA2dpService;-<init>-(Landroid/content/Context; Landroid/server/BluetoothService;)":
    "BLUETOOTH",
    "Landroid/server/BluetoothA2dpService;-addAudioSink-(Landroid/bluetooth/BluetoothDevice;)":
    "BLUETOOTH",
    "Landroid/server/BluetoothA2dpService;-getConnectedSinks-()": "BLUETOOTH",
    "Landroid/server/BluetoothA2dpService;-getNonDisconnectedSinks-()": "BLUETOOTH",
    "Landroid/server/BluetoothA2dpService;-getSinkPriority-(Landroid/bluetooth/BluetoothDevice;)":
    "BLUETOOTH",
    "Landroid/server/BluetoothA2dpService;-getSinkState-(Landroid/bluetooth/BluetoothDevice;)":
    "BLUETOOTH",
    "Landroid/server/BluetoothA2dpService;-isSinkDevice-(Landroid/bluetooth/BluetoothDevice;)":
    "BLUETOOTH",
    "Landroid/server/BluetoothA2dpService;-lookupSinksMatchingStates-([I)": "BLUETOOTH",
    "Landroid/server/BluetoothA2dpService;-onConnectSinkResult-(Ljava/lang/String; B)":
    "BLUETOOTH",
    "Landroid/server/BluetoothA2dpService;-onSinkPropertyChanged-(Ljava/lang/String; [L[Ljava/lang/Strin;)":
    "BLUETOOTH",
    "Landroid/provider/Settings/Secure;-BLUETOOTH_ON-Ljava/lang/String;": "BLUETOOTH",
    "Landroid/bluetooth/IBluetoothPbap$Stub$Proxy;-getClient-()": "BLUETOOTH",
    "Landroid/bluetooth/IBluetoothPbap$Stub$Proxy;-getState-()": "BLUETOOTH",
    "Landroid/bluetooth/IBluetoothPbap$Stub$Proxy;-isConnected-(Landroid/bluetooth/BluetoothDevice;)":
    "BLUETOOTH",
    "Landroid/server/BluetoothService;-addRemoteDeviceProperties-(Ljava/lang/String; [L[Ljava/lang/Strin;)":
    "BLUETOOTH",
    "Landroid/server/BluetoothService;-addRfcommServiceRecord-(Ljava/lang/String; Landroid/os/ParcelUuid; I Landroid/os/IBinder;)":
    "BLUETOOTH",
    "Landroid/server/BluetoothService;-fetchRemoteUuids-(Ljava/lang/String; Landroid/os/ParcelUuid; Landroid/bluetooth/IBluetoothCallback;)":
    "BLUETOOTH",
    "Landroid/server/BluetoothService;-getAddress-()": "BLUETOOTH",
    "Landroid/server/BluetoothService;-getAddressFromObjectPath-(Ljava/lang/String;)":
    "BLUETOOTH",
    "Landroid/server/BluetoothService;-getAllProperties-()": "BLUETOOTH",
    "Landroid/server/BluetoothService;-getBluetoothState-()": "BLUETOOTH",
    "Landroid/server/BluetoothService;-getBondState-(Ljava/lang/String;)": "BLUETOOTH",
    "Landroid/server/BluetoothService;-getDiscoverableTimeout-()": "BLUETOOTH",
    "Landroid/server/BluetoothService;-getName-()": "BLUETOOTH",
    "Landroid/server/BluetoothService;-getObjectPathFromAddress-(Ljava/lang/String;)":
    "BLUETOOTH",
    "Landroid/server/BluetoothService;-getProperty-(Ljava/lang/String;)": "BLUETOOTH",
    "Landroid/server/BluetoothService;-getPropertyInternal-(Ljava/lang/String;)":
    "BLUETOOTH",
    "Landroid/server/BluetoothService;-getRemoteClass-(Ljava/lang/String;)": "BLUETOOTH",
    "Landroid/server/BluetoothService;-getRemoteName-(Ljava/lang/String;)": "BLUETOOTH",
    "Landroid/server/BluetoothService;-getRemoteServiceChannel-(Ljava/lang/String; Landroid/os/ParcelUuid;)":
    "BLUETOOTH",
    "Landroid/server/BluetoothService;-getRemoteUuids-(Ljava/lang/String;)": "BLUETOOTH",
    "Landroid/server/BluetoothService;-getScanMode-()": "BLUETOOTH",
    "Landroid/server/BluetoothService;-getTrustState-(Ljava/lang/String;)": "BLUETOOTH",
    "Landroid/server/BluetoothService;-isDiscovering-()": "BLUETOOTH",
    "Landroid/server/BluetoothService;-isEnabled-()": "BLUETOOTH",
    "Landroid/server/BluetoothService;-listBonds-()": "BLUETOOTH",
    "Landroid/server/BluetoothService;-removeServiceRecord-(I)": "BLUETOOTH",
    "Landroid/server/BluetoothService;-sendUuidIntent-(Ljava/lang/String;)": "BLUETOOTH",
    "Landroid/server/BluetoothService;-setLinkTimeout-(Ljava/lang/String; I)": "BLUETOOTH",
    "Landroid/server/BluetoothService;-setPropertyBoolean-(Ljava/lang/String; B)":
    "BLUETOOTH",
    "Landroid/server/BluetoothService;-setPropertyInteger-(Ljava/lang/String; I)":
    "BLUETOOTH",
    "Landroid/server/BluetoothService;-setPropertyString-(Ljava/lang/String; Ljava/lang/String;)":
    "BLUETOOTH",
    "Landroid/server/BluetoothService;-updateDeviceServiceChannelCache-(Ljava/lang/String;)":
    "BLUETOOTH",
    "Landroid/server/BluetoothService;-updateRemoteDevicePropertiesCache-(Ljava/lang/String;)":
    "BLUETOOTH",
    "Landroid/content/pm/PackageManager;-FEATURE_BLUETOOTH-Ljava/lang/String;": "BLUETOOTH",
    "Landroid/bluetooth/BluetoothAssignedNumbers;-BLUETOOTH_SIG-I": "BLUETOOTH",
    "Landroid/app/ActivityManagerNative;-clearApplicationUserData-(Ljava/lang/String; Landroid/content/pm/IPackageDataObserver;)":
    "CLEAR_APP_USER_DATA",
    "Landroid/app/ContextImpl$ApplicationPackageManager;-clearApplicationUserData-(Ljava/lang/String; LIPackageDataObserver;)":
    "CLEAR_APP_USER_DATA",
    "Landroid/app/ContextImpl$ApplicationPackageManager;-clearApplicationUserData-(Ljava/lang/String; LIPackageDataObserver;)":
    "CLEAR_APP_USER_DATA",
    "Landroid/app/ActivityManager;-clearApplicationUserData-(Ljava/lang/String; Landroid/content/pm/IPackageDataObserver;)":
    "CLEAR_APP_USER_DATA",
    "Landroid/app/IActivityManager$Stub$Proxy;-clearApplicationUserData-(Ljava/lang/String; Landroid/content/pm/IPackageDataObserver;)":
    "CLEAR_APP_USER_DATA",
    "Landroid/content/pm/PackageManager;-clearApplicationUserData-(Ljava/lang/String; LIPackageDataObserver;)":
    "CLEAR_APP_USER_DATA",
    "Landroid/content/pm/IPackageManager$Stub$Proxy;-clearApplicationUserData-(Ljava/lang/String; Landroid/content/pm/IPackageDataObserver;)":
    "CLEAR_APP_USER_DATA",
    "Landroid/provider/Telephony$Sms;-addMessageToUri-(Landroid/content/ContentResolver; Landroid/net/Uri; Ljava/lang/String; Ljava/lang/String; Ljava/lang/String; Ljava/lang/Long; B B J)":
    "WRITE_SMS",
    "Landroid/provider/Telephony$Sms;-addMessageToUri-(Landroid/content/ContentResolver; Landroid/net/Uri; Ljava/lang/String; Ljava/lang/String; Ljava/lang/String; Ljava/lang/Long; B B)":
    "WRITE_SMS",
    "Landroid/provider/Telephony$Sms;-moveMessageToFolder-(Landroid/content/Context; Landroid/net/Uri; I I)":
    "WRITE_SMS",
    "Landroid/provider/Telephony$Sms$Outbox;-addMessage-(Landroid/content/ContentResolver; Ljava/lang/String; Ljava/lang/String; Ljava/lang/String; Ljava/lang/Long; B J)":
    "WRITE_SMS",
    "Landroid/provider/Telephony$Sms$Draft;-saveMessage-(Landroid/content/ContentResolver; Landroid/net/Uri; Ljava/lang/String;)":
    "WRITE_SMS",
    "Landroid/app/IActivityManager$Stub$Proxy;-setProcessForeground-(Landroid/os/IBinder; I B)":
    "SET_PROCESS_LIMIT",
    "Landroid/app/IActivityManager$Stub$Proxy;-setProcessLimit-(I)": "SET_PROCESS_LIMIT",
    "Landroid/os/PowerManager;-goToSleep-(J)": "DEVICE_POWER",
    "Landroid/os/PowerManager;-setBacklightBrightness-(I)": "DEVICE_POWER",
    "Landroid/os/IPowerManager$Stub$Proxy;-clearUserActivityTimeout-(J J)": "DEVICE_POWER",
    "Landroid/os/IPowerManager$Stub$Proxy;-goToSleep-(J)": "DEVICE_POWER",
    "Landroid/os/IPowerManager$Stub$Proxy;-goToSleepWithReason-(J I)": "DEVICE_POWER",
    "Landroid/os/IPowerManager$Stub$Proxy;-preventScreenOn-(B)": "DEVICE_POWER",
    "Landroid/os/IPowerManager$Stub$Proxy;-setAttentionLight-(B I)": "DEVICE_POWER",
    "Landroid/os/IPowerManager$Stub$Proxy;-setBacklightBrightness-(I)": "DEVICE_POWER",
    "Landroid/os/IPowerManager$Stub$Proxy;-setPokeLock-(I Landroid/os/IBinder; Ljava/lang/String;)":
    "DEVICE_POWER",
    "Landroid/os/IPowerManager$Stub$Proxy;-userActivityWithForce-(J B B)": "DEVICE_POWER",
    "Landroid/app/ExpandableListActivity;-setPersistent-(B)": "PERSISTENT_ACTIVITY",
    "Landroid/accounts/GrantCredentialsPermissionActivity;-setPersistent-(B)":
    "PERSISTENT_ACTIVITY",
    "Landroid/app/Activity;-setPersistent-(B)": "PERSISTENT_ACTIVITY",
    "Landroid/app/ListActivity;-setPersistent-(B)": "PERSISTENT_ACTIVITY",
    "Landroid/app/AliasActivity;-setPersistent-(B)": "PERSISTENT_ACTIVITY",
    "Landroid/accounts/AccountAuthenticatorActivity;-setPersistent-(B)":
    "PERSISTENT_ACTIVITY",
    "Landroid/app/IActivityManager$Stub$Proxy;-setPersistent-(Landroid/os/IBinder; B)":
    "PERSISTENT_ACTIVITY",
    "Landroid/app/TabActivity;-setPersistent-(B)": "PERSISTENT_ACTIVITY",
    "Landroid/app/ActivityGroup;-setPersistent-(B)": "PERSISTENT_ACTIVITY",
    "Landroid/view/IWindowManager$Stub$Proxy;-addAppToken-(I Landroid/view/IApplicationToken; I I B)":
    "MANAGE_APP_TOKENS",
    "Landroid/view/IWindowManager$Stub$Proxy;-addWindowToken-(Landroid/os/IBinder; I)":
    "MANAGE_APP_TOKENS",
    "Landroid/view/IWindowManager$Stub$Proxy;-executeAppTransition-()": "MANAGE_APP_TOKENS",
    "Landroid/view/IWindowManager$Stub$Proxy;-moveAppToken-(I Landroid/os/IBinder;)":
    "MANAGE_APP_TOKENS",
    "Landroid/view/IWindowManager$Stub$Proxy;-moveAppTokensToBottom-(Ljava/util/List;)":
    "MANAGE_APP_TOKENS",
    "Landroid/view/IWindowManager$Stub$Proxy;-moveAppTokensToTop-(Ljava/util/List;)":
    "MANAGE_APP_TOKENS",
    "Landroid/view/IWindowManager$Stub$Proxy;-pauseKeyDispatching-(Landroid/os/IBinder;)":
    "MANAGE_APP_TOKENS",
    "Landroid/view/IWindowManager$Stub$Proxy;-prepareAppTransition-(I)": "MANAGE_APP_TOKENS",
    "Landroid/view/IWindowManager$Stub$Proxy;-removeAppToken-(Landroid/os/IBinder;)":
    "MANAGE_APP_TOKENS",
    "Landroid/view/IWindowManager$Stub$Proxy;-removeWindowToken-(Landroid/os/IBinder;)":
    "MANAGE_APP_TOKENS",
    "Landroid/view/IWindowManager$Stub$Proxy;-resumeKeyDispatching-(Landroid/os/IBinder;)":
    "MANAGE_APP_TOKENS",
    "Landroid/view/IWindowManager$Stub$Proxy;-setAppGroupId-(Landroid/os/IBinder; I)":
    "MANAGE_APP_TOKENS",
    "Landroid/view/IWindowManager$Stub$Proxy;-setAppOrientation-(Landroid/view/IApplicationToken; I)":
    "MANAGE_APP_TOKENS",
    "Landroid/view/IWindowManager$Stub$Proxy;-setAppStartingWindow-(Landroid/os/IBinder; Ljava/lang/String; I Ljava/lang/CharSequence; I I Landroid/os/IBinder; B)":
    "MANAGE_APP_TOKENS",
    "Landroid/view/IWindowManager$Stub$Proxy;-setAppVisibility-(Landroid/os/IBinder; B)":
    "MANAGE_APP_TOKENS",
    "Landroid/view/IWindowManager$Stub$Proxy;-setAppWillBeHidden-(Landroid/os/IBinder;)":
    "MANAGE_APP_TOKENS",
    "Landroid/view/IWindowManager$Stub$Proxy;-setEventDispatching-(B)": "MANAGE_APP_TOKENS",
    "Landroid/view/IWindowManager$Stub$Proxy;-setFocusedApp-(Landroid/os/IBinder; B)":
    "MANAGE_APP_TOKENS",
    "Landroid/view/IWindowManager$Stub$Proxy;-setNewConfiguration-(Landroid/content/res/Configuration;)":
    "MANAGE_APP_TOKENS",
    "Landroid/view/IWindowManager$Stub$Proxy;-startAppFreezingScreen-(Landroid/os/IBinder; I)":
    "MANAGE_APP_TOKENS",
    "Landroid/view/IWindowManager$Stub$Proxy;-stopAppFreezingScreen-(Landroid/os/IBinder; B)":
    "MANAGE_APP_TOKENS",
    "Landroid/view/IWindowManager$Stub$Proxy;-updateOrientationFromAppTokens-(Landroid/content/res/Configuration; Landroid/os/IBinder;)":
    "MANAGE_APP_TOKENS",
    "Landroid/provider/Browser;-BOOKMARKS_URI-Landroid/net/Uri;": "WRITE_HISTORY_BOOKMARKS",
    "Landroid/provider/Browser;-SEARCHES_URI-Landroid/net/Uri;": "WRITE_HISTORY_BOOKMARKS",
    "Landroid/provider/Browser;-addSearchUrl-(Landroid/content/ContentResolver; Ljava/lang/String;)":
    "WRITE_HISTORY_BOOKMARKS",
    "Landroid/provider/Browser;-clearHistory-(Landroid/content/ContentResolver;)":
    "WRITE_HISTORY_BOOKMARKS",
    "Landroid/provider/Browser;-clearSearches-(Landroid/content/ContentResolver;)":
    "WRITE_HISTORY_BOOKMARKS",
    "Landroid/provider/Browser;-deleteFromHistory-(Landroid/content/ContentResolver; Ljava/lang/String;)":
    "WRITE_HISTORY_BOOKMARKS",
    "Landroid/provider/Browser;-deleteHistoryTimeFrame-(Landroid/content/ContentResolver; J J)":
    "WRITE_HISTORY_BOOKMARKS",
    "Landroid/provider/Browser;-truncateHistory-(Landroid/content/ContentResolver;)":
    "WRITE_HISTORY_BOOKMARKS",
    "Landroid/provider/Browser;-updateVisitedHistory-(Landroid/content/ContentResolver; Ljava/lang/String; B)":
    "WRITE_HISTORY_BOOKMARKS",
    "Landroid/provider/Browser;-clearSearches-(Landroid/content/ContentResolver;)":
    "WRITE_HISTORY_BOOKMARKS",
    "Landroid/app/IActivityManager$Stub$Proxy;-unhandledBack-(I)": "FORCE_BACK",
    "Landroid/net/IConnectivityManager$Stub$Proxy;-requestRouteToHost-(I I)":
    "CHANGE_NETWORK_STATE",
    "Landroid/net/IConnectivityManager$Stub$Proxy;-setMobileDataEnabled-(B)":
    "CHANGE_NETWORK_STATE",
    "Landroid/net/IConnectivityManager$Stub$Proxy;-setNetworkPreference-(I)":
    "CHANGE_NETWORK_STATE",
    "Landroid/net/IConnectivityManager$Stub$Proxy;-setRadio-(I B)": "CHANGE_NETWORK_STATE",
    "Landroid/net/IConnectivityManager$Stub$Proxy;-setRadios-(B)": "CHANGE_NETWORK_STATE",
    "Landroid/net/IConnectivityManager$Stub$Proxy;-stopUsingNetworkFeature-(I Ljava/lang/String;)":
    "CHANGE_NETWORK_STATE",
    "Landroid/net/IConnectivityManager$Stub$Proxy;-tether-(Ljava/lang/String;)":
    "CHANGE_NETWORK_STATE",
    "Landroid/net/IConnectivityManager$Stub$Proxy;-untether-(Ljava/lang/String;)":
    "CHANGE_NETWORK_STATE",
    "Landroid/net/ConnectivityManager;-requestRouteToHost-(I I)": "CHANGE_NETWORK_STATE",
    "Landroid/net/ConnectivityManager;-setMobileDataEnabled-(B)": "CHANGE_NETWORK_STATE",
    "Landroid/net/ConnectivityManager;-setNetworkPreference-(I)": "CHANGE_NETWORK_STATE",
    "Landroid/net/ConnectivityManager;-setRadio-(I B)": "CHANGE_NETWORK_STATE",
    "Landroid/net/ConnectivityManager;-setRadios-(B)": "CHANGE_NETWORK_STATE",
    "Landroid/net/ConnectivityManager;-startUsingNetworkFeature-(I Ljava/lang/String;)":
    "CHANGE_NETWORK_STATE",
    "Landroid/net/ConnectivityManager;-stopUsingNetworkFeature-(I Ljava/lang/String;)":
    "CHANGE_NETWORK_STATE",
    "Landroid/net/ConnectivityManager;-tether-(Ljava/lang/String;)": "CHANGE_NETWORK_STATE",
    "Landroid/net/ConnectivityManager;-untether-(Ljava/lang/String;)": "CHANGE_NETWORK_STATE",
    "Landroid/os/INetworkManagementService$Stub$Proxy;-attachPppd-(Ljava/lang/String; Ljava/lang/String; Ljava/lang/String; Ljava/lang/String; Ljava/lang/String;)":
    "CHANGE_NETWORK_STATE",
    "Landroid/os/INetworkManagementService$Stub$Proxy;-detachPppd-(Ljava/lang/String;)":
    "CHANGE_NETWORK_STATE",
    "Landroid/os/INetworkManagementService$Stub$Proxy;-disableNat-(Ljava/lang/String; Ljava/lang/String;)":
    "CHANGE_NETWORK_STATE",
    "Landroid/os/INetworkManagementService$Stub$Proxy;-enableNat-(Ljava/lang/String; Ljava/lang/String;)":
    "CHANGE_NETWORK_STATE",
    "Landroid/os/INetworkManagementService$Stub$Proxy;-setAccessPoint-(Landroid/net/wifi/WifiConfiguration; Ljava/lang/String; Ljava/lang/String;)":
    "CHANGE_NETWORK_STATE",
    "Landroid/os/INetworkManagementService$Stub$Proxy;-setInterfaceThrottle-(Ljava/lang/String; I I)":
    "CHANGE_NETWORK_STATE",
    "Landroid/os/INetworkManagementService$Stub$Proxy;-setIpForwardingEnabled-(B)":
    "CHANGE_NETWORK_STATE",
    "Landroid/os/INetworkManagementService$Stub$Proxy;-startAccessPoint-(Landroid/net/wifi/WifiConfiguration; Ljava/lang/String; Ljava/lang/String;)":
    "CHANGE_NETWORK_STATE",
    "Landroid/os/INetworkManagementService$Stub$Proxy;-startUsbRNDIS-()":
    "CHANGE_NETWORK_STATE",
    "Landroid/os/INetworkManagementService$Stub$Proxy;-stopAccessPoint-()":
    "CHANGE_NETWORK_STATE",
    "Landroid/os/INetworkManagementService$Stub$Proxy;-stopTethering-()":
    "CHANGE_NETWORK_STATE",
    "Landroid/os/INetworkManagementService$Stub$Proxy;-stopUsbRNDIS-()":
    "CHANGE_NETWORK_STATE",
    "Landroid/os/INetworkManagementService$Stub$Proxy;-tetherInterface-(Ljava/lang/String;)":
    "CHANGE_NETWORK_STATE",
    "Landroid/os/INetworkManagementService$Stub$Proxy;-unregisterObserver-(Landroid/net/INetworkManagementEventObserver;)":
    "CHANGE_NETWORK_STATE",
    "Landroid/os/INetworkManagementService$Stub$Proxy;-untetherInterface-(Ljava/lang/String;)":
    "CHANGE_NETWORK_STATE",
    "Landroid/app/ContextImpl$ApplicationContentResolver;-addPeriodicSync-(Landroid/accounts/Account; Ljava/lang/String; Landroid/os/Bundle; J)":
    "WRITE_SYNC_SETTINGS",
    "Landroid/app/ContextImpl$ApplicationContentResolver;-removePeriodicSync-(Landroid/accounts/Account; Ljava/lang/String; Landroid/os/Bundle;)":
    "WRITE_SYNC_SETTINGS",
    "Landroid/app/ContextImpl$ApplicationContentResolver;-setIsSyncable-(Landroid/accounts/Account; Ljava/lang/String; I)":
    "WRITE_SYNC_SETTINGS",
    "Landroid/app/ContextImpl$ApplicationContentResolver;-setMasterSyncAutomatically-(B)":
    "WRITE_SYNC_SETTINGS",
    "Landroid/app/ContextImpl$ApplicationContentResolver;-setSyncAutomatically-(Landroid/accounts/Account; Ljava/lang/String; B)":
    "WRITE_SYNC_SETTINGS",
    "Landroid/content/ContentService;-addPeriodicSync-(Landroid/accounts/Account; Ljava/lang/String; Landroid/os/Bundle; J)":
    "WRITE_SYNC_SETTINGS",
    "Landroid/content/ContentService;-removePeriodicSync-(Landroid/accounts/Account; Ljava/lang/String; Landroid/os/Bundle;)":
    "WRITE_SYNC_SETTINGS",
    "Landroid/content/ContentService;-setIsSyncable-(Landroid/accounts/Account; Ljava/lang/String; I)":
    "WRITE_SYNC_SETTINGS",
    "Landroid/content/ContentService;-setMasterSyncAutomatically-(B)": "WRITE_SYNC_SETTINGS",
    "Landroid/content/ContentService;-setSyncAutomatically-(Landroid/accounts/Account; Ljava/lang/String; B)":
    "WRITE_SYNC_SETTINGS",
    "Landroid/content/ContentResolver;-addPeriodicSync-(Landroid/accounts/Account; Ljava/lang/String; Landroid/os/Bundle; J)":
    "WRITE_SYNC_SETTINGS",
    "Landroid/content/ContentResolver;-removePeriodicSync-(Landroid/accounts/Account; Ljava/lang/String; Landroid/os/Bundle;)":
    "WRITE_SYNC_SETTINGS",
    "Landroid/content/ContentResolver;-setIsSyncable-(Landroid/accounts/Account; Ljava/lang/String; I)":
    "WRITE_SYNC_SETTINGS",
    "Landroid/content/ContentResolver;-setMasterSyncAutomatically-(B)": "WRITE_SYNC_SETTINGS",
    "Landroid/content/ContentResolver;-setSyncAutomatically-(Landroid/accounts/Account; Ljava/lang/String; B)":
    "WRITE_SYNC_SETTINGS",
    "Landroid/content/IContentService$Stub$Proxy;-addPeriodicSync-(Landroid/accounts/Account; Ljava/lang/String; Landroid/os/Bundle; J)":
    "WRITE_SYNC_SETTINGS",
    "Landroid/content/IContentService$Stub$Proxy;-removePeriodicSync-(Landroid/accounts/Account; Ljava/lang/String; Landroid/os/Bundle;)":
    "WRITE_SYNC_SETTINGS",
    "Landroid/content/IContentService$Stub$Proxy;-setIsSyncable-(Landroid/accounts/Account; Ljava/lang/String; I)":
    "WRITE_SYNC_SETTINGS",
    "Landroid/content/IContentService$Stub$Proxy;-setMasterSyncAutomatically-(B)":
    "WRITE_SYNC_SETTINGS",
    "Landroid/content/IContentService$Stub$Proxy;-setSyncAutomatically-(Landroid/accounts/Account; Ljava/lang/String; B)":
    "WRITE_SYNC_SETTINGS",
    "Landroid/accounts/AccountManager;-KEY_ACCOUNT_MANAGER_RESPONSE-Ljava/lang/String;":
    "ACCOUNT_MANAGER",
    "Landroid/accounts/AbstractAccountAuthenticator;-checkBinderPermission-()":
    "ACCOUNT_MANAGER",
    "Landroid/accounts/AbstractAccountAuthenticator;-confirmCredentials-(Landroid/accounts/IAccountAuthenticatorResponse; Landroid/accounts/Account; Landroid/os/Bundle;)":
    "ACCOUNT_MANAGER",
    "Landroid/accounts/AbstractAccountAuthenticator;-editProperties-(Landroid/accounts/IAccountAuthenticatorResponse; Ljava/lang/String;)":
    "ACCOUNT_MANAGER",
    "Landroid/accounts/AbstractAccountAuthenticator;-getAccountRemovalAllowed-(Landroid/accounts/IAccountAuthenticatorResponse; Landroid/accounts/Account;)":
    "ACCOUNT_MANAGER",
    "Landroid/accounts/AbstractAccountAuthenticator;-getAuthToken-(Landroid/accounts/IAccountAuthenticatorResponse; Landroid/accounts/Account; Ljava/lang/String; Landroid/os/Bundle;)":
    "ACCOUNT_MANAGER",
    "Landroid/accounts/AbstractAccountAuthenticator;-getAuthTokenLabel-(Landroid/accounts/IAccountAuthenticatorResponse; Ljava/lang/String;)":
    "ACCOUNT_MANAGER",
    "Landroid/accounts/AbstractAccountAuthenticator;-hasFeatures-(Landroid/accounts/IAccountAuthenticatorResponse; Landroid/accounts/Account; [L[Ljava/lang/Strin;)":
    "ACCOUNT_MANAGER",
    "Landroid/accounts/AbstractAccountAuthenticator;-updateCredentials-(Landroid/accounts/IAccountAuthenticatorResponse; Landroid/accounts/Account; Ljava/lang/String; Landroid/os/Bundle;)":
    "ACCOUNT_MANAGER",
    "Landroid/accounts/AbstractAccountAuthenticator;-addAccount-(Landroid/accounts/IAccountAuthenticatorResponse; Ljava/lang/String; Ljava/lang/String; [L[Ljava/lang/Strin; Landroid/os/Bundle;)":
    "ACCOUNT_MANAGER",
    "Landroid/accounts/AbstractAccountAuthenticator$Transport;-addAccount-(Landroid/accounts/IAccountAuthenticatorResponse; Ljava/lang/String; Ljava/lang/String; [L[Ljava/lang/Strin; Landroid/os/Bundle;)":
    "ACCOUNT_MANAGER",
    "Landroid/accounts/AbstractAccountAuthenticator$Transport;-confirmCredentials-(Landroid/accounts/IAccountAuthenticatorResponse; Landroid/accounts/Account; Landroid/os/Bundle;)":
    "ACCOUNT_MANAGER",
    "Landroid/accounts/AbstractAccountAuthenticator$Transport;-editProperties-(Landroid/accounts/IAccountAuthenticatorResponse; Ljava/lang/String;)":
    "ACCOUNT_MANAGER",
    "Landroid/accounts/AbstractAccountAuthenticator$Transport;-getAccountRemovalAllowed-(Landroid/accounts/IAccountAuthenticatorResponse; Landroid/accounts/Account;)":
    "ACCOUNT_MANAGER",
    "Landroid/accounts/AbstractAccountAuthenticator$Transport;-getAuthToken-(Landroid/accounts/IAccountAuthenticatorResponse; Landroid/accounts/Account; Ljava/lang/String; Landroid/os/Bundle;)":
    "ACCOUNT_MANAGER",
    "Landroid/accounts/AbstractAccountAuthenticator$Transport;-getAuthTokenLabel-(Landroid/accounts/IAccountAuthenticatorResponse; Ljava/lang/String;)":
    "ACCOUNT_MANAGER",
    "Landroid/accounts/AbstractAccountAuthenticator$Transport;-hasFeatures-(Landroid/accounts/IAccountAuthenticatorResponse; Landroid/accounts/Account; [L[Ljava/lang/Strin;)":
    "ACCOUNT_MANAGER",
    "Landroid/accounts/AbstractAccountAuthenticator$Transport;-updateCredentials-(Landroid/accounts/IAccountAuthenticatorResponse; Landroid/accounts/Account; Ljava/lang/String; Landroid/os/Bundle;)":
    "ACCOUNT_MANAGER",
    "Landroid/accounts/IAccountAuthenticator$Stub$Proxy;-addAccount-(Landroid/accounts/IAccountAuthenticatorResponse; Ljava/lang/String; Ljava/lang/String; [L[Ljava/lang/Strin; Landroid/os/Bundle;)":
    "ACCOUNT_MANAGER",
    "Landroid/accounts/IAccountAuthenticator$Stub$Proxy;-confirmCredentials-(Landroid/accounts/IAccountAuthenticatorResponse; Landroid/accounts/Account; Landroid/os/Bundle;)":
    "ACCOUNT_MANAGER",
    "Landroid/accounts/IAccountAuthenticator$Stub$Proxy;-editProperties-(Landroid/accounts/IAccountAuthenticatorResponse; Ljava/lang/String;)":
    "ACCOUNT_MANAGER",
    "Landroid/accounts/IAccountAuthenticator$Stub$Proxy;-getAccountRemovalAllowed-(Landroid/accounts/IAccountAuthenticatorResponse; Landroid/accounts/Account;)":
    "ACCOUNT_MANAGER",
    "Landroid/accounts/IAccountAuthenticator$Stub$Proxy;-getAuthToken-(Landroid/accounts/IAccountAuthenticatorResponse; Landroid/accounts/Account; Ljava/lang/String; Landroid/os/Bundle;)":
    "ACCOUNT_MANAGER",
    "Landroid/accounts/IAccountAuthenticator$Stub$Proxy;-getAuthTokenLabel-(Landroid/accounts/IAccountAuthenticatorResponse; Ljava/lang/String;)":
    "ACCOUNT_MANAGER",
    "Landroid/accounts/IAccountAuthenticator$Stub$Proxy;-hasFeatures-(Landroid/accounts/IAccountAuthenticatorResponse; Landroid/accounts/Account; [L[Ljava/lang/Strin;)":
    "ACCOUNT_MANAGER",
    "Landroid/accounts/IAccountAuthenticator$Stub$Proxy;-updateCredentials-(Landroid/accounts/IAccountAuthenticatorResponse; Landroid/accounts/Account; Ljava/lang/String; Landroid/os/Bundle;)":
    "ACCOUNT_MANAGER",
    "Landroid/view/IWindowManager$Stub$Proxy;-setAnimationScale-(I F)": "SET_ANIMATION_SCALE",
    "Landroid/view/IWindowManager$Stub$Proxy;-setAnimationScales-([L;)": "SET_ANIMATION_SCALE",
    "Landroid/accounts/AccountManager;-getAccounts-()": "GET_ACCOUNTS",
    "Landroid/accounts/AccountManager;-getAccountsByType-(Ljava/lang/String;)": "GET_ACCOUNTS",
    "Landroid/accounts/AccountManager;-getAccountsByTypeAndFeatures-(Ljava/lang/String; [Ljava/lang/String; [Landroid/accounts/AccountManagerCallback<android/accounts/Account[; Landroid/os/Handler;)":
    "GET_ACCOUNTS",
    "Landroid/accounts/AccountManager;-hasFeatures-(Landroid/accounts/Account; [Ljava/lang/String; Landroid/accounts/AccountManagerCallback<java/lang/Boolean>; Landroid/os/Handler;)":
    "GET_ACCOUNTS",
    "Landroid/accounts/AccountManager;-addOnAccountsUpdatedListener-(Landroid/accounts/OnAccountsUpdateListener; Landroid/os/Handler; B)":
    "GET_ACCOUNTS",
    "Landroid/accounts/AccountManager;-getAccounts-()": "GET_ACCOUNTS",
    "Landroid/accounts/AccountManager;-getAccountsByType-(Ljava/lang/String;)": "GET_ACCOUNTS",
    "Landroid/accounts/AccountManager;-getAccountsByTypeAndFeatures-(Ljava/lang/String; [L[Ljava/lang/Strin; Landroid/accounts/AccountManagerCallback; Landroid/os/Handler;)":
    "GET_ACCOUNTS",
    "Landroid/accounts/AccountManager;-getAuthTokenByFeatures-(Ljava/lang/String; Ljava/lang/String; [L[Ljava/lang/Strin; Landroid/app/Activity; Landroid/os/Bundle; Landroid/os/Bundle; Landroid/accounts/AccountManagerCallback; Landroid/os/Handler;)":
    "GET_ACCOUNTS",
    "Landroid/accounts/AccountManager;-hasFeatures-(Landroid/accounts/Account; [L[Ljava/lang/Strin; Landroid/accounts/AccountManagerCallback; Landroid/os/Handler;)":
    "GET_ACCOUNTS",
    "Landroid/content/ContentService;-<init>-(Landroid/content/Context; B)": "GET_ACCOUNTS",
    "Landroid/content/ContentService;-main-(Landroid/content/Context; B)": "GET_ACCOUNTS",
    "Landroid/accounts/AccountManager$GetAuthTokenByTypeAndFeaturesTask;-doWork-()":
    "GET_ACCOUNTS",
    "Landroid/accounts/AccountManager$GetAuthTokenByTypeAndFeaturesTask;-start-()":
    "GET_ACCOUNTS",
    "Landroid/accounts/AccountManager$AmsTask;-doWork-()": "GET_ACCOUNTS",
    "Landroid/accounts/AccountManager$AmsTask;-start-()": "GET_ACCOUNTS",
    "Landroid/accounts/IAccountManager$Stub$Proxy;-getAccounts-(Ljava/lang/String;)":
    "GET_ACCOUNTS",
    "Landroid/accounts/IAccountManager$Stub$Proxy;-getAccountsByFeatures-(Landroid/accounts/IAccountManagerResponse; Ljava/lang/String; [L[Ljava/lang/Strin;)":
    "GET_ACCOUNTS",
    "Landroid/accounts/IAccountManager$Stub$Proxy;-hasFeatures-(Landroid/accounts/IAccountManagerResponse; Landroid/accounts/Account; [L[Ljava/lang/Strin;)":
    "GET_ACCOUNTS",
    "Landroid/accounts/AccountManagerService;-checkReadAccountsPermission-()": "GET_ACCOUNTS",
    "Landroid/accounts/AccountManagerService;-getAccounts-(Ljava/lang/String;)":
    "GET_ACCOUNTS",
    "Landroid/accounts/AccountManagerService;-getAccountsByFeatures-(Landroid/accounts/IAccountManagerResponse; Ljava/lang/String; [L[Ljava/lang/Strin;)":
    "GET_ACCOUNTS",
    "Landroid/accounts/AccountManagerService;-hasFeatures-(Landroid/accounts/IAccountManagerResponse; Landroid/accounts/Account; [L[Ljava/lang/Strin;)":
    "GET_ACCOUNTS",
    "Landroid/telephony/gsm/SmsManager;-copyMessageToSim-([L; [L; I)": "RECEIVE_SMS",
    "Landroid/telephony/gsm/SmsManager;-deleteMessageFromSim-(I)": "RECEIVE_SMS",
    "Landroid/telephony/gsm/SmsManager;-getAllMessagesFromSim-()": "RECEIVE_SMS",
    "Landroid/telephony/gsm/SmsManager;-updateMessageOnSim-(I I [L;)": "RECEIVE_SMS",
    "Landroid/telephony/SmsManager;-copyMessageToIcc-([L; [L; I)": "RECEIVE_SMS",
    "Landroid/telephony/SmsManager;-deleteMessageFromIcc-(I)": "RECEIVE_SMS",
    "Landroid/telephony/SmsManager;-getAllMessagesFromIcc-()": "RECEIVE_SMS",
    "Landroid/telephony/SmsManager;-updateMessageOnIcc-(I I [L;)": "RECEIVE_SMS",
    "Lcom/android/internal/telephony/ISms$Stub$Proxy;-copyMessageToIccEf-(I [B [B)":
    "RECEIVE_SMS",
    "Lcom/android/internal/telephony/ISms$Stub$Proxy;-getAllMessagesFromIccEf-()":
    "RECEIVE_SMS",
    "Lcom/android/internal/telephony/ISms$Stub$Proxy;-updateMessageOnIccEf-(I I [B)":
    "RECEIVE_SMS",
    "Landroid/app/IActivityManager$Stub$Proxy;-resumeAppSwitches-()": "STOP_APP_SWITCHES",
    "Landroid/app/IActivityManager$Stub$Proxy;-stopAppSwitches-()": "STOP_APP_SWITCHES",
    "Landroid/app/ContextImpl$ApplicationPackageManager;-deleteApplicationCacheFiles-(Ljava/lang/String; LIPackageDataObserver;)":
    "DELETE_CACHE_FILES",
    "Landroid/app/ContextImpl$ApplicationPackageManager;-deleteApplicationCacheFiles-(Ljava/lang/String; Landroid/content/pm/IPackageDataObserver;)":
    "DELETE_CACHE_FILES",
    "Landroid/content/pm/PackageManager;-deleteApplicationCacheFiles-(Ljava/lang/String; Landroid/content/pm/IPackageDataObserver;)":
    "DELETE_CACHE_FILES",
    "Landroid/content/pm/IPackageManager$Stub$Proxy;-deleteApplicationCacheFiles-(Ljava/lang/String; Landroid/content/pm/IPackageDataObserver;)":
    "DELETE_CACHE_FILES",
    "Landroid/os/Build/VERSION_CODES;-DONUT-I": "WRITE_EXTERNAL_STORAGE",
    "Landroid/app/DownloadManager/Request;-setDestinationUri-(Landroid/net/Uri;)":
    "WRITE_EXTERNAL_STORAGE",
    "Landroid/os/RecoverySystem;-installPackage-(Landroid/content/Context; Ljava/io/File;)":
    "REBOOT",
    "Landroid/os/RecoverySystem;-rebootWipeUserData-(Landroid/content/Context;)": "REBOOT",
    "Landroid/os/RecoverySystem;-bootCommand-(Landroid/content/Context; Ljava/lang/String;)":
    "REBOOT",
    "Landroid/os/RecoverySystem;-installPackage-(Landroid/content/Context; Ljava/io/File;)":
    "REBOOT",
    "Landroid/os/RecoverySystem;-rebootWipeUserData-(Landroid/content/Context;)": "REBOOT",
    "Landroid/content/Intent;-IntentResolution-Ljava/lang/String;": "REBOOT",
    "Landroid/content/Intent;-ACTION_REBOOT-Ljava/lang/String;": "REBOOT",
    "Landroid/os/PowerManager;-reboot-(Ljava/lang/String;)": "REBOOT",
    "Landroid/os/PowerManager;-reboot-(Ljava/lang/String;)": "REBOOT",
    "Landroid/os/IPowerManager$Stub$Proxy;-crash-(Ljava/lang/String;)": "REBOOT",
    "Landroid/os/IPowerManager$Stub$Proxy;-reboot-(Ljava/lang/String;)": "REBOOT",
    "Landroid/app/ContextImpl$ApplicationPackageManager;-installPackage-(Landroid/net/Uri; LIPackageInstallObserver; I Ljava/lang/String;)":
    "INSTALL_PACKAGES",
    "Landroid/app/ContextImpl$ApplicationPackageManager;-installPackage-(Landroid/net/Uri; LIPackageInstallObserver; I Ljava/lang/String;)":
    "INSTALL_PACKAGES",
    "Landroid/content/pm/PackageManager;-installPackage-(Landroid/net/Uri; LIPackageInstallObserver; I Ljava/lang/String;)":
    "INSTALL_PACKAGES",
    "Landroid/content/pm/IPackageManager$Stub$Proxy;-installPackage-(Landroid/net/Uri; Landroid/content/pm/IPackageInstallObserver; I Ljava/lang/String;)":
    "INSTALL_PACKAGES",
    "Landroid/app/IActivityManager$Stub$Proxy;-setDebugApp-(Ljava/lang/String; B B)":
    "SET_DEBUG_APP",
    "Landroid/location/ILocationManager$Stub$Proxy;-reportLocation-(Landroid/location/Location; B)":
    "INSTALL_LOCATION_PROVIDER",
    "Landroid/app/WallpaperManager;-suggestDesiredDimensions-(I I)": "SET_WALLPAPER_HINTS",
    "Landroid/app/IWallpaperManager$Stub$Proxy;-setDimensionHints-(I I)": "SET_WALLPAPER_HINTS",
    "Landroid/app/ContextImpl$ApplicationContentResolver;-openFileDescriptor-(Landroid/net/Uri; Ljava/lang/String;)":
    "READ_CONTACTS",
    "Landroid/app/ContextImpl$ApplicationContentResolver;-openInputStream-(Landroid/net/Uri;)":
    "READ_CONTACTS",
    "Landroid/app/ContextImpl$ApplicationContentResolver;-openOutputStream-(Landroid/net/Uri;)":
    "READ_CONTACTS",
    "Landroid/app/ContextImpl$ApplicationContentResolver;-query-(Landroid/net/Uri; [L[Ljava/lang/Strin; Ljava/lang/String; [L[Ljava/lang/Strin; Ljava/lang/String;)":
    "READ_CONTACTS",
    "Lcom/android/internal/telephony/IccPhoneBookInterfaceManager$Stub$Proxy;-getAdnRecordsInEf-(I)":
    "READ_CONTACTS",
    "Landroid/provider/Contacts$People;-addToGroup-(Landroid/content/ContentResolver; J Ljava/lang/String;)":
    "READ_CONTACTS",
    "Landroid/provider/Contacts$People;-addToMyContactsGroup-(Landroid/content/ContentResolver; J)":
    "READ_CONTACTS",
    "Landroid/provider/Contacts$People;-createPersonInMyContactsGroup-(Landroid/content/ContentResolver; Landroid/content/ContentValues;)":
    "READ_CONTACTS",
    "Landroid/provider/Contacts$People;-loadContactPhoto-(Landroid/content/Context; Landroid/net/Uri; I Landroid/graphics/BitmapFactory$Options;)":
    "READ_CONTACTS",
    "Landroid/provider/Contacts$People;-markAsContacted-(Landroid/content/ContentResolver; J)":
    "READ_CONTACTS",
    "Landroid/provider/Contacts$People;-openContactPhotoInputStream-(Landroid/content/ContentResolver; Landroid/net/Uri;)":
    "READ_CONTACTS",
    "Landroid/provider/Contacts$People;-queryGroups-(Landroid/content/ContentResolver; J)":
    "READ_CONTACTS",
    "Landroid/provider/Contacts$People;-setPhotoData-(Landroid/content/ContentResolver; Landroid/net/Uri; [L;)":
    "READ_CONTACTS",
    "Landroid/provider/Contacts$People;-tryGetMyContactsGroupId-(Landroid/content/ContentResolver;)":
    "READ_CONTACTS",
    "Landroid/provider/ContactsContract$Data;-getContactLookupUri-(Landroid/content/ContentResolver; Landroid/net/Uri;)":
    "READ_CONTACTS",
    "Landroid/provider/ContactsContract$Contacts;-getLookupUri-(Landroid/content/ContentResolver; Landroid/net/Uri;)":
    "READ_CONTACTS",
    "Landroid/provider/ContactsContract$Contacts;-lookupContact-(Landroid/content/ContentResolver; Landroid/net/Uri;)":
    "READ_CONTACTS",
    "Landroid/provider/ContactsContract$Contacts;-openContactPhotoInputStream-(Landroid/content/ContentResolver; Landroid/net/Uri;)":
    "READ_CONTACTS",
    "Landroid/pim/vcard/VCardComposer;-createOneEntry-()": "READ_CONTACTS",
    "Landroid/pim/vcard/VCardComposer;-createOneEntry-(Ljava/lang/reflect/Method;)":
    "READ_CONTACTS",
    "Landroid/pim/vcard/VCardComposer;-createOneEntryInternal-(Ljava/lang/String; Ljava/lang/reflect/Method;)":
    "READ_CONTACTS",
    "Landroid/pim/vcard/VCardComposer;-init-()": "READ_CONTACTS",
    "Landroid/pim/vcard/VCardComposer;-init-(Ljava/lang/String; [L[Ljava/lang/Strin;)":
    "READ_CONTACTS",
    "Landroid/pim/vcard/VCardComposer$OneEntryHandler;-onInit-(Landroid/content/Context;)":
    "READ_CONTACTS",
    "Lcom/android/internal/telephony/CallerInfo;-getCallerId-(Landroid/content/Context; Ljava/lang/String;)":
    "READ_CONTACTS",
    "Lcom/android/internal/telephony/CallerInfo;-getCallerInfo-(Landroid/content/Context; Ljava/lang/String;)":
    "READ_CONTACTS",
    "Landroid/provider/Contacts$Settings;-getSetting-(Landroid/content/ContentResolver; Ljava/lang/String; Ljava/lang/String;)":
    "READ_CONTACTS",
    "Landroid/provider/ContactsContract$RawContacts;-getContactLookupUri-(Landroid/content/ContentResolver; Landroid/net/Uri;)":
    "READ_CONTACTS",
    "Landroid/provider/CallLog$Calls;-addCall-(Lcom/android/internal/telephony/CallerInfo; Landroid/content/Context; Ljava/lang/String; I I J I)":
    "READ_CONTACTS",
    "Landroid/provider/CallLog$Calls;-getLastOutgoingCall-(Landroid/content/Context;)":
    "READ_CONTACTS",
    "Lcom/android/internal/telephony/IIccPhoneBook$Stub$Proxy;-getAdnRecordsInEf-(I)":
    "READ_CONTACTS",
    "Landroid/pim/vcard/VCardComposer$HandlerForOutputStream;-onInit-(Landroid/content/Context;)":
    "READ_CONTACTS",
    "Landroid/provider/ContactsContract$CommonDataKinds$Phone;-CONTENT_URI-Landroid/net/Uri;":
    "READ_CONTACTS",
    "Landroid/widget/QuickContactBadge;-assignContactFromEmail-(Ljava/lang/String; B)":
    "READ_CONTACTS",
    "Landroid/widget/QuickContactBadge;-assignContactFromPhone-(Ljava/lang/String; B)":
    "READ_CONTACTS",
    "Landroid/widget/QuickContactBadge;-trigger-(Landroid/net/Uri;)": "READ_CONTACTS",
    "Landroid/content/ContentResolver;-openFileDescriptor-(Landroid/net/Uri; Ljava/lang/String;)":
    "READ_CONTACTS",
    "Landroid/content/ContentResolver;-openInputStream-(Landroid/net/Uri;)": "READ_CONTACTS",
    "Landroid/content/ContentResolver;-openOutputStream-(Landroid/net/Uri;)": "READ_CONTACTS",
    "Landroid/content/ContentResolver;-query-(Landroid/net/Uri; [L[Ljava/lang/Strin; Ljava/lang/String; [L[Ljava/lang/Strin; Ljava/lang/String;)":
    "READ_CONTACTS",
    "Landroid/app/backup/IBackupManager$Stub$Proxy;-backupNow-()": "BACKUP",
    "Landroid/app/backup/IBackupManager$Stub$Proxy;-beginRestoreSession-(Ljava/lang/String;)":
    "BACKUP",
    "Landroid/app/backup/IBackupManager$Stub$Proxy;-clearBackupData-(Ljava/lang/String;)":
    "BACKUP",
    "Landroid/app/backup/IBackupManager$Stub$Proxy;-dataChanged-(Ljava/lang/String;)": "BACKUP",
    "Landroid/app/backup/IBackupManager$Stub$Proxy;-getCurrentTransport-()": "BACKUP",
    "Landroid/app/backup/IBackupManager$Stub$Proxy;-isBackupEnabled-()": "BACKUP",
    "Landroid/app/backup/IBackupManager$Stub$Proxy;-listAllTransports-()": "BACKUP",
    "Landroid/app/backup/IBackupManager$Stub$Proxy;-selectBackupTransport-(Ljava/lang/String;)":
    "BACKUP",
    "Landroid/app/backup/IBackupManager$Stub$Proxy;-setAutoRestore-(B)": "BACKUP",
    "Landroid/app/backup/IBackupManager$Stub$Proxy;-setBackupEnabled-(B)": "BACKUP",
    "Landroid/app/IActivityManager$Stub$Proxy;-bindBackupAgent-(Landroid/content/pm/ApplicationInfo; I)":
    "BACKUP",
    "Landroid/app/backup/BackupManager;-beginRestoreSession-()": "BACKUP",
    "Landroid/app/backup/BackupManager;-dataChanged-(Ljava/lang/String;)": "BACKUP",
    "Landroid/app/backup/BackupManager;-requestRestore-(Landroid/app/backup/RestoreObserver;)":
    "BACKUP",
}
