
@0x941bafde6c08a5ac;
struct Schema {
	mountNamespace @0 :Text;
	mountMountpoint @1 :Text;
	mountMode @2 :Text = "ro";
	mountTrimbase @3 :Bool = true;
	mountFlist @4 :Text;
	mountTrim @5 :Text;
	backendPath @6 :Text;
	backendNamespace @7 :Text;
	backendUpload @8 :Bool = false;
	backendEncrypted @9 :Bool = false;
	backendUserRsa @10 :Text;
	backendStoreRsa @11 :Text;
	backendPush @12 :Text;
	backendCleanupCron @13 :Text;
	backendCleanupOld @14 :Int64 = 0;
	storeUrl @15 :Text;
	storeLogin @16 :Text;
	storePassword @17 :Text;

}
