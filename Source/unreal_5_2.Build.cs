// Copyright Epic Games, Inc. All Rights Reserved.

using UnrealBuildTool;

public class unreal_5_2 : ModuleRules
{
	public unreal_5_2(ReadOnlyTargetRules Target) : base(Target)
	{
		PCHUsage = PCHUsageMode.UseExplicitOrSharedPCHs;
	
		PublicDependencyModuleNames.AddRange(new string[] { "Core", "CoreUObject", "Engine", "InputCore", "Sockets", "Networking", "Json", "JsonUtilities" });

		PrivateDependencyModuleNames.AddRange(new string[] {  });
	}
}
