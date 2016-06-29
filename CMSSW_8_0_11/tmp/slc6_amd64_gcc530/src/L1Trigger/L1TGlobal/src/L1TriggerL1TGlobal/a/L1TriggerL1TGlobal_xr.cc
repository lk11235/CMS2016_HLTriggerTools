// Do NOT change. Changes will be lost next time file is generated

#define R__DICTIONARY_FILENAME tmpdIslc6_amd64_gcc530dIsrcdIL1TriggerdIL1TGlobaldIsrcdIL1TriggerL1TGlobaldIadIL1TriggerL1TGlobal_xr

/*******************************************************************/
#include <stddef.h>
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>
#include <assert.h>
#define G__DICTIONARY
#include "RConfig.h"
#include "TClass.h"
#include "TDictAttributeMap.h"
#include "TInterpreter.h"
#include "TROOT.h"
#include "TBuffer.h"
#include "TMemberInspector.h"
#include "TInterpreter.h"
#include "TVirtualMutex.h"
#include "TError.h"

#ifndef G__ROOT
#define G__ROOT
#endif

#include "RtypesImp.h"
#include "TIsAProxy.h"
#include "TFileMergeInfo.h"
#include <algorithm>
#include "TCollectionProxyInfo.h"
/*******************************************************************/

#include "TDataMember.h"

// Since CINT ignores the std namespace, we need to do so in this file.
namespace std {} using namespace std;

// Header files passed as explicit arguments
#include "src/L1Trigger/L1TGlobal/src/classes.h"

// Header files passed via #pragma extra_include

namespace ROOT {
   static TClass *CorrelationTemplate_Dictionary();
   static void CorrelationTemplate_TClassManip(TClass*);
   static void *new_CorrelationTemplate(void *p = 0);
   static void *newArray_CorrelationTemplate(Long_t size, void *p);
   static void delete_CorrelationTemplate(void *p);
   static void deleteArray_CorrelationTemplate(void *p);
   static void destruct_CorrelationTemplate(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const ::CorrelationTemplate*)
   {
      ::CorrelationTemplate *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TIsAProxy(typeid(::CorrelationTemplate));
      static ::ROOT::TGenericClassInfo 
         instance("CorrelationTemplate", "L1Trigger/L1TGlobal/interface/CorrelationTemplate.h", 36,
                  typeid(::CorrelationTemplate), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &CorrelationTemplate_Dictionary, isa_proxy, 0,
                  sizeof(::CorrelationTemplate) );
      instance.SetNew(&new_CorrelationTemplate);
      instance.SetNewArray(&newArray_CorrelationTemplate);
      instance.SetDelete(&delete_CorrelationTemplate);
      instance.SetDeleteArray(&deleteArray_CorrelationTemplate);
      instance.SetDestructor(&destruct_CorrelationTemplate);
      return &instance;
   }
   TGenericClassInfo *GenerateInitInstance(const ::CorrelationTemplate*)
   {
      return GenerateInitInstanceLocal((::CorrelationTemplate*)0);
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_(Init) = GenerateInitInstanceLocal((const ::CorrelationTemplate*)0x0); R__UseDummy(_R__UNIQUE_(Init));

   // Dictionary for non-ClassDef classes
   static TClass *CorrelationTemplate_Dictionary() {
      TClass* theClass =::ROOT::GenerateInitInstanceLocal((const ::CorrelationTemplate*)0x0)->GetClass();
      CorrelationTemplate_TClassManip(theClass);
   return theClass;
   }

   static void CorrelationTemplate_TClassManip(TClass* ){
   }

} // end of namespace ROOT

namespace ROOT {
   static TClass *CorrelationTemplatecLcLCorrelationParameter_Dictionary();
   static void CorrelationTemplatecLcLCorrelationParameter_TClassManip(TClass*);
   static void *new_CorrelationTemplatecLcLCorrelationParameter(void *p = 0);
   static void *newArray_CorrelationTemplatecLcLCorrelationParameter(Long_t size, void *p);
   static void delete_CorrelationTemplatecLcLCorrelationParameter(void *p);
   static void deleteArray_CorrelationTemplatecLcLCorrelationParameter(void *p);
   static void destruct_CorrelationTemplatecLcLCorrelationParameter(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const ::CorrelationTemplate::CorrelationParameter*)
   {
      ::CorrelationTemplate::CorrelationParameter *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TIsAProxy(typeid(::CorrelationTemplate::CorrelationParameter));
      static ::ROOT::TGenericClassInfo 
         instance("CorrelationTemplate::CorrelationParameter", "L1Trigger/L1TGlobal/interface/CorrelationTemplate.h", 67,
                  typeid(::CorrelationTemplate::CorrelationParameter), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &CorrelationTemplatecLcLCorrelationParameter_Dictionary, isa_proxy, 0,
                  sizeof(::CorrelationTemplate::CorrelationParameter) );
      instance.SetNew(&new_CorrelationTemplatecLcLCorrelationParameter);
      instance.SetNewArray(&newArray_CorrelationTemplatecLcLCorrelationParameter);
      instance.SetDelete(&delete_CorrelationTemplatecLcLCorrelationParameter);
      instance.SetDeleteArray(&deleteArray_CorrelationTemplatecLcLCorrelationParameter);
      instance.SetDestructor(&destruct_CorrelationTemplatecLcLCorrelationParameter);
      return &instance;
   }
   TGenericClassInfo *GenerateInitInstance(const ::CorrelationTemplate::CorrelationParameter*)
   {
      return GenerateInitInstanceLocal((::CorrelationTemplate::CorrelationParameter*)0);
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_(Init) = GenerateInitInstanceLocal((const ::CorrelationTemplate::CorrelationParameter*)0x0); R__UseDummy(_R__UNIQUE_(Init));

   // Dictionary for non-ClassDef classes
   static TClass *CorrelationTemplatecLcLCorrelationParameter_Dictionary() {
      TClass* theClass =::ROOT::GenerateInitInstanceLocal((const ::CorrelationTemplate::CorrelationParameter*)0x0)->GetClass();
      CorrelationTemplatecLcLCorrelationParameter_TClassManip(theClass);
   return theClass;
   }

   static void CorrelationTemplatecLcLCorrelationParameter_TClassManip(TClass* ){
   }

} // end of namespace ROOT

namespace ROOT {
   static TClass *TriggerMenu_Dictionary();
   static void TriggerMenu_TClassManip(TClass*);
   static void *new_TriggerMenu(void *p = 0);
   static void *newArray_TriggerMenu(Long_t size, void *p);
   static void delete_TriggerMenu(void *p);
   static void deleteArray_TriggerMenu(void *p);
   static void destruct_TriggerMenu(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const ::TriggerMenu*)
   {
      ::TriggerMenu *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TIsAProxy(typeid(::TriggerMenu));
      static ::ROOT::TGenericClassInfo 
         instance("TriggerMenu", "L1Trigger/L1TGlobal/interface/TriggerMenu.h", 45,
                  typeid(::TriggerMenu), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &TriggerMenu_Dictionary, isa_proxy, 0,
                  sizeof(::TriggerMenu) );
      instance.SetNew(&new_TriggerMenu);
      instance.SetNewArray(&newArray_TriggerMenu);
      instance.SetDelete(&delete_TriggerMenu);
      instance.SetDeleteArray(&deleteArray_TriggerMenu);
      instance.SetDestructor(&destruct_TriggerMenu);
      return &instance;
   }
   TGenericClassInfo *GenerateInitInstance(const ::TriggerMenu*)
   {
      return GenerateInitInstanceLocal((::TriggerMenu*)0);
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_(Init) = GenerateInitInstanceLocal((const ::TriggerMenu*)0x0); R__UseDummy(_R__UNIQUE_(Init));

   // Dictionary for non-ClassDef classes
   static TClass *TriggerMenu_Dictionary() {
      TClass* theClass =::ROOT::GenerateInitInstanceLocal((const ::TriggerMenu*)0x0)->GetClass();
      TriggerMenu_TClassManip(theClass);
   return theClass;
   }

   static void TriggerMenu_TClassManip(TClass* theClass){
      theClass->CreateAttributeMap();
      TDictAttributeMap* attrMap( theClass->GetAttributeMap() );
      attrMap->AddProperty("class_version","TriggerMenu_V01");
      TDataMember* theMember_m_vecMuonTemplate = theClass->GetDataMember("m_vecMuonTemplate");
      theMember_m_vecMuonTemplate->CreateAttributeMap();
      TDictAttributeMap* memberAttrMap_m_vecMuonTemplate( theMember_m_vecMuonTemplate->GetAttributeMap() );
      memberAttrMap_m_vecMuonTemplate->AddProperty("mapping","blob");
      TDataMember* theMember_m_vecCaloTemplate = theClass->GetDataMember("m_vecCaloTemplate");
      theMember_m_vecCaloTemplate->CreateAttributeMap();
      TDictAttributeMap* memberAttrMap_m_vecCaloTemplate( theMember_m_vecCaloTemplate->GetAttributeMap() );
      memberAttrMap_m_vecCaloTemplate->AddProperty("mapping","blob");
      TDataMember* theMember_m_vecEnergySumTemplate = theClass->GetDataMember("m_vecEnergySumTemplate");
      theMember_m_vecEnergySumTemplate->CreateAttributeMap();
      TDictAttributeMap* memberAttrMap_m_vecEnergySumTemplate( theMember_m_vecEnergySumTemplate->GetAttributeMap() );
      memberAttrMap_m_vecEnergySumTemplate->AddProperty("mapping","blob");
      TDataMember* theMember_m_vecExternalTemplate = theClass->GetDataMember("m_vecExternalTemplate");
      theMember_m_vecExternalTemplate->CreateAttributeMap();
      TDictAttributeMap* memberAttrMap_m_vecExternalTemplate( theMember_m_vecExternalTemplate->GetAttributeMap() );
      memberAttrMap_m_vecExternalTemplate->AddProperty("mapping","blob");
      TDataMember* theMember_m_vecCorrelationTemplate = theClass->GetDataMember("m_vecCorrelationTemplate");
      theMember_m_vecCorrelationTemplate->CreateAttributeMap();
      TDictAttributeMap* memberAttrMap_m_vecCorrelationTemplate( theMember_m_vecCorrelationTemplate->GetAttributeMap() );
      memberAttrMap_m_vecCorrelationTemplate->AddProperty("mapping","blob");
      TDataMember* theMember_m_corMuonTemplate = theClass->GetDataMember("m_corMuonTemplate");
      theMember_m_corMuonTemplate->CreateAttributeMap();
      TDictAttributeMap* memberAttrMap_m_corMuonTemplate( theMember_m_corMuonTemplate->GetAttributeMap() );
      memberAttrMap_m_corMuonTemplate->AddProperty("mapping","blob");
      TDataMember* theMember_m_corCaloTemplate = theClass->GetDataMember("m_corCaloTemplate");
      theMember_m_corCaloTemplate->CreateAttributeMap();
      TDictAttributeMap* memberAttrMap_m_corCaloTemplate( theMember_m_corCaloTemplate->GetAttributeMap() );
      memberAttrMap_m_corCaloTemplate->AddProperty("mapping","blob");
      TDataMember* theMember_m_corEnergySumTemplate = theClass->GetDataMember("m_corEnergySumTemplate");
      theMember_m_corEnergySumTemplate->CreateAttributeMap();
      TDictAttributeMap* memberAttrMap_m_corEnergySumTemplate( theMember_m_corEnergySumTemplate->GetAttributeMap() );
      memberAttrMap_m_corEnergySumTemplate->AddProperty("mapping","blob");
      TDataMember* theMember_m_algorithmMap = theClass->GetDataMember("m_algorithmMap");
      theMember_m_algorithmMap->CreateAttributeMap();
      TDictAttributeMap* memberAttrMap_m_algorithmMap( theMember_m_algorithmMap->GetAttributeMap() );
      memberAttrMap_m_algorithmMap->AddProperty("mapping","blob");
      TDataMember* theMember_m_algorithmAliasMap = theClass->GetDataMember("m_algorithmAliasMap");
      theMember_m_algorithmAliasMap->CreateAttributeMap();
      TDictAttributeMap* memberAttrMap_m_algorithmAliasMap( theMember_m_algorithmAliasMap->GetAttributeMap() );
      memberAttrMap_m_algorithmAliasMap->AddProperty("mapping","blob");
   }

} // end of namespace ROOT

namespace ROOT {
   static TClass *MuonTemplate_Dictionary();
   static void MuonTemplate_TClassManip(TClass*);
   static void *new_MuonTemplate(void *p = 0);
   static void *newArray_MuonTemplate(Long_t size, void *p);
   static void delete_MuonTemplate(void *p);
   static void deleteArray_MuonTemplate(void *p);
   static void destruct_MuonTemplate(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const ::MuonTemplate*)
   {
      ::MuonTemplate *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TIsAProxy(typeid(::MuonTemplate));
      static ::ROOT::TGenericClassInfo 
         instance("MuonTemplate", "L1Trigger/L1TGlobal/interface/MuonTemplate.h", 32,
                  typeid(::MuonTemplate), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &MuonTemplate_Dictionary, isa_proxy, 0,
                  sizeof(::MuonTemplate) );
      instance.SetNew(&new_MuonTemplate);
      instance.SetNewArray(&newArray_MuonTemplate);
      instance.SetDelete(&delete_MuonTemplate);
      instance.SetDeleteArray(&deleteArray_MuonTemplate);
      instance.SetDestructor(&destruct_MuonTemplate);
      return &instance;
   }
   TGenericClassInfo *GenerateInitInstance(const ::MuonTemplate*)
   {
      return GenerateInitInstanceLocal((::MuonTemplate*)0);
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_(Init) = GenerateInitInstanceLocal((const ::MuonTemplate*)0x0); R__UseDummy(_R__UNIQUE_(Init));

   // Dictionary for non-ClassDef classes
   static TClass *MuonTemplate_Dictionary() {
      TClass* theClass =::ROOT::GenerateInitInstanceLocal((const ::MuonTemplate*)0x0)->GetClass();
      MuonTemplate_TClassManip(theClass);
   return theClass;
   }

   static void MuonTemplate_TClassManip(TClass* ){
   }

} // end of namespace ROOT

namespace ROOT {
   static TClass *MuonTemplatecLcLObjectParameter_Dictionary();
   static void MuonTemplatecLcLObjectParameter_TClassManip(TClass*);
   static void *new_MuonTemplatecLcLObjectParameter(void *p = 0);
   static void *newArray_MuonTemplatecLcLObjectParameter(Long_t size, void *p);
   static void delete_MuonTemplatecLcLObjectParameter(void *p);
   static void deleteArray_MuonTemplatecLcLObjectParameter(void *p);
   static void destruct_MuonTemplatecLcLObjectParameter(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const ::MuonTemplate::ObjectParameter*)
   {
      ::MuonTemplate::ObjectParameter *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TIsAProxy(typeid(::MuonTemplate::ObjectParameter));
      static ::ROOT::TGenericClassInfo 
         instance("MuonTemplate::ObjectParameter", "L1Trigger/L1TGlobal/interface/MuonTemplate.h", 58,
                  typeid(::MuonTemplate::ObjectParameter), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &MuonTemplatecLcLObjectParameter_Dictionary, isa_proxy, 0,
                  sizeof(::MuonTemplate::ObjectParameter) );
      instance.SetNew(&new_MuonTemplatecLcLObjectParameter);
      instance.SetNewArray(&newArray_MuonTemplatecLcLObjectParameter);
      instance.SetDelete(&delete_MuonTemplatecLcLObjectParameter);
      instance.SetDeleteArray(&deleteArray_MuonTemplatecLcLObjectParameter);
      instance.SetDestructor(&destruct_MuonTemplatecLcLObjectParameter);
      return &instance;
   }
   TGenericClassInfo *GenerateInitInstance(const ::MuonTemplate::ObjectParameter*)
   {
      return GenerateInitInstanceLocal((::MuonTemplate::ObjectParameter*)0);
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_(Init) = GenerateInitInstanceLocal((const ::MuonTemplate::ObjectParameter*)0x0); R__UseDummy(_R__UNIQUE_(Init));

   // Dictionary for non-ClassDef classes
   static TClass *MuonTemplatecLcLObjectParameter_Dictionary() {
      TClass* theClass =::ROOT::GenerateInitInstanceLocal((const ::MuonTemplate::ObjectParameter*)0x0)->GetClass();
      MuonTemplatecLcLObjectParameter_TClassManip(theClass);
   return theClass;
   }

   static void MuonTemplatecLcLObjectParameter_TClassManip(TClass* ){
   }

} // end of namespace ROOT

namespace ROOT {
   static TClass *MuonTemplatecLcLCorrelationParameter_Dictionary();
   static void MuonTemplatecLcLCorrelationParameter_TClassManip(TClass*);
   static void *new_MuonTemplatecLcLCorrelationParameter(void *p = 0);
   static void *newArray_MuonTemplatecLcLCorrelationParameter(Long_t size, void *p);
   static void delete_MuonTemplatecLcLCorrelationParameter(void *p);
   static void deleteArray_MuonTemplatecLcLCorrelationParameter(void *p);
   static void destruct_MuonTemplatecLcLCorrelationParameter(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const ::MuonTemplate::CorrelationParameter*)
   {
      ::MuonTemplate::CorrelationParameter *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TIsAProxy(typeid(::MuonTemplate::CorrelationParameter));
      static ::ROOT::TGenericClassInfo 
         instance("MuonTemplate::CorrelationParameter", "L1Trigger/L1TGlobal/interface/MuonTemplate.h", 87,
                  typeid(::MuonTemplate::CorrelationParameter), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &MuonTemplatecLcLCorrelationParameter_Dictionary, isa_proxy, 0,
                  sizeof(::MuonTemplate::CorrelationParameter) );
      instance.SetNew(&new_MuonTemplatecLcLCorrelationParameter);
      instance.SetNewArray(&newArray_MuonTemplatecLcLCorrelationParameter);
      instance.SetDelete(&delete_MuonTemplatecLcLCorrelationParameter);
      instance.SetDeleteArray(&deleteArray_MuonTemplatecLcLCorrelationParameter);
      instance.SetDestructor(&destruct_MuonTemplatecLcLCorrelationParameter);
      return &instance;
   }
   TGenericClassInfo *GenerateInitInstance(const ::MuonTemplate::CorrelationParameter*)
   {
      return GenerateInitInstanceLocal((::MuonTemplate::CorrelationParameter*)0);
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_(Init) = GenerateInitInstanceLocal((const ::MuonTemplate::CorrelationParameter*)0x0); R__UseDummy(_R__UNIQUE_(Init));

   // Dictionary for non-ClassDef classes
   static TClass *MuonTemplatecLcLCorrelationParameter_Dictionary() {
      TClass* theClass =::ROOT::GenerateInitInstanceLocal((const ::MuonTemplate::CorrelationParameter*)0x0)->GetClass();
      MuonTemplatecLcLCorrelationParameter_TClassManip(theClass);
   return theClass;
   }

   static void MuonTemplatecLcLCorrelationParameter_TClassManip(TClass* ){
   }

} // end of namespace ROOT

namespace ROOT {
   static TClass *CaloTemplate_Dictionary();
   static void CaloTemplate_TClassManip(TClass*);
   static void *new_CaloTemplate(void *p = 0);
   static void *newArray_CaloTemplate(Long_t size, void *p);
   static void delete_CaloTemplate(void *p);
   static void deleteArray_CaloTemplate(void *p);
   static void destruct_CaloTemplate(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const ::CaloTemplate*)
   {
      ::CaloTemplate *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TIsAProxy(typeid(::CaloTemplate));
      static ::ROOT::TGenericClassInfo 
         instance("CaloTemplate", "L1Trigger/L1TGlobal/interface/CaloTemplate.h", 32,
                  typeid(::CaloTemplate), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &CaloTemplate_Dictionary, isa_proxy, 0,
                  sizeof(::CaloTemplate) );
      instance.SetNew(&new_CaloTemplate);
      instance.SetNewArray(&newArray_CaloTemplate);
      instance.SetDelete(&delete_CaloTemplate);
      instance.SetDeleteArray(&deleteArray_CaloTemplate);
      instance.SetDestructor(&destruct_CaloTemplate);
      return &instance;
   }
   TGenericClassInfo *GenerateInitInstance(const ::CaloTemplate*)
   {
      return GenerateInitInstanceLocal((::CaloTemplate*)0);
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_(Init) = GenerateInitInstanceLocal((const ::CaloTemplate*)0x0); R__UseDummy(_R__UNIQUE_(Init));

   // Dictionary for non-ClassDef classes
   static TClass *CaloTemplate_Dictionary() {
      TClass* theClass =::ROOT::GenerateInitInstanceLocal((const ::CaloTemplate*)0x0)->GetClass();
      CaloTemplate_TClassManip(theClass);
   return theClass;
   }

   static void CaloTemplate_TClassManip(TClass* ){
   }

} // end of namespace ROOT

namespace ROOT {
   static TClass *CaloTemplatecLcLObjectParameter_Dictionary();
   static void CaloTemplatecLcLObjectParameter_TClassManip(TClass*);
   static void *new_CaloTemplatecLcLObjectParameter(void *p = 0);
   static void *newArray_CaloTemplatecLcLObjectParameter(Long_t size, void *p);
   static void delete_CaloTemplatecLcLObjectParameter(void *p);
   static void deleteArray_CaloTemplatecLcLObjectParameter(void *p);
   static void destruct_CaloTemplatecLcLObjectParameter(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const ::CaloTemplate::ObjectParameter*)
   {
      ::CaloTemplate::ObjectParameter *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TIsAProxy(typeid(::CaloTemplate::ObjectParameter));
      static ::ROOT::TGenericClassInfo 
         instance("CaloTemplate::ObjectParameter", "L1Trigger/L1TGlobal/interface/CaloTemplate.h", 58,
                  typeid(::CaloTemplate::ObjectParameter), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &CaloTemplatecLcLObjectParameter_Dictionary, isa_proxy, 0,
                  sizeof(::CaloTemplate::ObjectParameter) );
      instance.SetNew(&new_CaloTemplatecLcLObjectParameter);
      instance.SetNewArray(&newArray_CaloTemplatecLcLObjectParameter);
      instance.SetDelete(&delete_CaloTemplatecLcLObjectParameter);
      instance.SetDeleteArray(&deleteArray_CaloTemplatecLcLObjectParameter);
      instance.SetDestructor(&destruct_CaloTemplatecLcLObjectParameter);
      return &instance;
   }
   TGenericClassInfo *GenerateInitInstance(const ::CaloTemplate::ObjectParameter*)
   {
      return GenerateInitInstanceLocal((::CaloTemplate::ObjectParameter*)0);
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_(Init) = GenerateInitInstanceLocal((const ::CaloTemplate::ObjectParameter*)0x0); R__UseDummy(_R__UNIQUE_(Init));

   // Dictionary for non-ClassDef classes
   static TClass *CaloTemplatecLcLObjectParameter_Dictionary() {
      TClass* theClass =::ROOT::GenerateInitInstanceLocal((const ::CaloTemplate::ObjectParameter*)0x0)->GetClass();
      CaloTemplatecLcLObjectParameter_TClassManip(theClass);
   return theClass;
   }

   static void CaloTemplatecLcLObjectParameter_TClassManip(TClass* ){
   }

} // end of namespace ROOT

namespace ROOT {
   static TClass *CaloTemplatecLcLCorrelationParameter_Dictionary();
   static void CaloTemplatecLcLCorrelationParameter_TClassManip(TClass*);
   static void *new_CaloTemplatecLcLCorrelationParameter(void *p = 0);
   static void *newArray_CaloTemplatecLcLCorrelationParameter(Long_t size, void *p);
   static void delete_CaloTemplatecLcLCorrelationParameter(void *p);
   static void deleteArray_CaloTemplatecLcLCorrelationParameter(void *p);
   static void destruct_CaloTemplatecLcLCorrelationParameter(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const ::CaloTemplate::CorrelationParameter*)
   {
      ::CaloTemplate::CorrelationParameter *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TIsAProxy(typeid(::CaloTemplate::CorrelationParameter));
      static ::ROOT::TGenericClassInfo 
         instance("CaloTemplate::CorrelationParameter", "L1Trigger/L1TGlobal/interface/CaloTemplate.h", 81,
                  typeid(::CaloTemplate::CorrelationParameter), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &CaloTemplatecLcLCorrelationParameter_Dictionary, isa_proxy, 0,
                  sizeof(::CaloTemplate::CorrelationParameter) );
      instance.SetNew(&new_CaloTemplatecLcLCorrelationParameter);
      instance.SetNewArray(&newArray_CaloTemplatecLcLCorrelationParameter);
      instance.SetDelete(&delete_CaloTemplatecLcLCorrelationParameter);
      instance.SetDeleteArray(&deleteArray_CaloTemplatecLcLCorrelationParameter);
      instance.SetDestructor(&destruct_CaloTemplatecLcLCorrelationParameter);
      return &instance;
   }
   TGenericClassInfo *GenerateInitInstance(const ::CaloTemplate::CorrelationParameter*)
   {
      return GenerateInitInstanceLocal((::CaloTemplate::CorrelationParameter*)0);
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_(Init) = GenerateInitInstanceLocal((const ::CaloTemplate::CorrelationParameter*)0x0); R__UseDummy(_R__UNIQUE_(Init));

   // Dictionary for non-ClassDef classes
   static TClass *CaloTemplatecLcLCorrelationParameter_Dictionary() {
      TClass* theClass =::ROOT::GenerateInitInstanceLocal((const ::CaloTemplate::CorrelationParameter*)0x0)->GetClass();
      CaloTemplatecLcLCorrelationParameter_TClassManip(theClass);
   return theClass;
   }

   static void CaloTemplatecLcLCorrelationParameter_TClassManip(TClass* ){
   }

} // end of namespace ROOT

namespace ROOT {
   // Wrappers around operator new
   static void *new_CorrelationTemplate(void *p) {
      return  p ? new(p) ::CorrelationTemplate : new ::CorrelationTemplate;
   }
   static void *newArray_CorrelationTemplate(Long_t nElements, void *p) {
      return p ? new(p) ::CorrelationTemplate[nElements] : new ::CorrelationTemplate[nElements];
   }
   // Wrapper around operator delete
   static void delete_CorrelationTemplate(void *p) {
      delete ((::CorrelationTemplate*)p);
   }
   static void deleteArray_CorrelationTemplate(void *p) {
      delete [] ((::CorrelationTemplate*)p);
   }
   static void destruct_CorrelationTemplate(void *p) {
      typedef ::CorrelationTemplate current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class ::CorrelationTemplate

namespace ROOT {
   // Wrappers around operator new
   static void *new_CorrelationTemplatecLcLCorrelationParameter(void *p) {
      return  p ? ::new((::ROOT::Internal::TOperatorNewHelper*)p) ::CorrelationTemplate::CorrelationParameter : new ::CorrelationTemplate::CorrelationParameter;
   }
   static void *newArray_CorrelationTemplatecLcLCorrelationParameter(Long_t nElements, void *p) {
      return p ? ::new((::ROOT::Internal::TOperatorNewHelper*)p) ::CorrelationTemplate::CorrelationParameter[nElements] : new ::CorrelationTemplate::CorrelationParameter[nElements];
   }
   // Wrapper around operator delete
   static void delete_CorrelationTemplatecLcLCorrelationParameter(void *p) {
      delete ((::CorrelationTemplate::CorrelationParameter*)p);
   }
   static void deleteArray_CorrelationTemplatecLcLCorrelationParameter(void *p) {
      delete [] ((::CorrelationTemplate::CorrelationParameter*)p);
   }
   static void destruct_CorrelationTemplatecLcLCorrelationParameter(void *p) {
      typedef ::CorrelationTemplate::CorrelationParameter current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class ::CorrelationTemplate::CorrelationParameter

namespace ROOT {
   // Wrappers around operator new
   static void *new_TriggerMenu(void *p) {
      return  p ? new(p) ::TriggerMenu : new ::TriggerMenu;
   }
   static void *newArray_TriggerMenu(Long_t nElements, void *p) {
      return p ? new(p) ::TriggerMenu[nElements] : new ::TriggerMenu[nElements];
   }
   // Wrapper around operator delete
   static void delete_TriggerMenu(void *p) {
      delete ((::TriggerMenu*)p);
   }
   static void deleteArray_TriggerMenu(void *p) {
      delete [] ((::TriggerMenu*)p);
   }
   static void destruct_TriggerMenu(void *p) {
      typedef ::TriggerMenu current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class ::TriggerMenu

namespace ROOT {
   // Wrappers around operator new
   static void *new_MuonTemplate(void *p) {
      return  p ? new(p) ::MuonTemplate : new ::MuonTemplate;
   }
   static void *newArray_MuonTemplate(Long_t nElements, void *p) {
      return p ? new(p) ::MuonTemplate[nElements] : new ::MuonTemplate[nElements];
   }
   // Wrapper around operator delete
   static void delete_MuonTemplate(void *p) {
      delete ((::MuonTemplate*)p);
   }
   static void deleteArray_MuonTemplate(void *p) {
      delete [] ((::MuonTemplate*)p);
   }
   static void destruct_MuonTemplate(void *p) {
      typedef ::MuonTemplate current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class ::MuonTemplate

namespace ROOT {
   // Wrappers around operator new
   static void *new_MuonTemplatecLcLObjectParameter(void *p) {
      return  p ? ::new((::ROOT::Internal::TOperatorNewHelper*)p) ::MuonTemplate::ObjectParameter : new ::MuonTemplate::ObjectParameter;
   }
   static void *newArray_MuonTemplatecLcLObjectParameter(Long_t nElements, void *p) {
      return p ? ::new((::ROOT::Internal::TOperatorNewHelper*)p) ::MuonTemplate::ObjectParameter[nElements] : new ::MuonTemplate::ObjectParameter[nElements];
   }
   // Wrapper around operator delete
   static void delete_MuonTemplatecLcLObjectParameter(void *p) {
      delete ((::MuonTemplate::ObjectParameter*)p);
   }
   static void deleteArray_MuonTemplatecLcLObjectParameter(void *p) {
      delete [] ((::MuonTemplate::ObjectParameter*)p);
   }
   static void destruct_MuonTemplatecLcLObjectParameter(void *p) {
      typedef ::MuonTemplate::ObjectParameter current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class ::MuonTemplate::ObjectParameter

namespace ROOT {
   // Wrappers around operator new
   static void *new_MuonTemplatecLcLCorrelationParameter(void *p) {
      return  p ? ::new((::ROOT::Internal::TOperatorNewHelper*)p) ::MuonTemplate::CorrelationParameter : new ::MuonTemplate::CorrelationParameter;
   }
   static void *newArray_MuonTemplatecLcLCorrelationParameter(Long_t nElements, void *p) {
      return p ? ::new((::ROOT::Internal::TOperatorNewHelper*)p) ::MuonTemplate::CorrelationParameter[nElements] : new ::MuonTemplate::CorrelationParameter[nElements];
   }
   // Wrapper around operator delete
   static void delete_MuonTemplatecLcLCorrelationParameter(void *p) {
      delete ((::MuonTemplate::CorrelationParameter*)p);
   }
   static void deleteArray_MuonTemplatecLcLCorrelationParameter(void *p) {
      delete [] ((::MuonTemplate::CorrelationParameter*)p);
   }
   static void destruct_MuonTemplatecLcLCorrelationParameter(void *p) {
      typedef ::MuonTemplate::CorrelationParameter current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class ::MuonTemplate::CorrelationParameter

namespace ROOT {
   // Wrappers around operator new
   static void *new_CaloTemplate(void *p) {
      return  p ? new(p) ::CaloTemplate : new ::CaloTemplate;
   }
   static void *newArray_CaloTemplate(Long_t nElements, void *p) {
      return p ? new(p) ::CaloTemplate[nElements] : new ::CaloTemplate[nElements];
   }
   // Wrapper around operator delete
   static void delete_CaloTemplate(void *p) {
      delete ((::CaloTemplate*)p);
   }
   static void deleteArray_CaloTemplate(void *p) {
      delete [] ((::CaloTemplate*)p);
   }
   static void destruct_CaloTemplate(void *p) {
      typedef ::CaloTemplate current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class ::CaloTemplate

namespace ROOT {
   // Wrappers around operator new
   static void *new_CaloTemplatecLcLObjectParameter(void *p) {
      return  p ? ::new((::ROOT::Internal::TOperatorNewHelper*)p) ::CaloTemplate::ObjectParameter : new ::CaloTemplate::ObjectParameter;
   }
   static void *newArray_CaloTemplatecLcLObjectParameter(Long_t nElements, void *p) {
      return p ? ::new((::ROOT::Internal::TOperatorNewHelper*)p) ::CaloTemplate::ObjectParameter[nElements] : new ::CaloTemplate::ObjectParameter[nElements];
   }
   // Wrapper around operator delete
   static void delete_CaloTemplatecLcLObjectParameter(void *p) {
      delete ((::CaloTemplate::ObjectParameter*)p);
   }
   static void deleteArray_CaloTemplatecLcLObjectParameter(void *p) {
      delete [] ((::CaloTemplate::ObjectParameter*)p);
   }
   static void destruct_CaloTemplatecLcLObjectParameter(void *p) {
      typedef ::CaloTemplate::ObjectParameter current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class ::CaloTemplate::ObjectParameter

namespace ROOT {
   // Wrappers around operator new
   static void *new_CaloTemplatecLcLCorrelationParameter(void *p) {
      return  p ? ::new((::ROOT::Internal::TOperatorNewHelper*)p) ::CaloTemplate::CorrelationParameter : new ::CaloTemplate::CorrelationParameter;
   }
   static void *newArray_CaloTemplatecLcLCorrelationParameter(Long_t nElements, void *p) {
      return p ? ::new((::ROOT::Internal::TOperatorNewHelper*)p) ::CaloTemplate::CorrelationParameter[nElements] : new ::CaloTemplate::CorrelationParameter[nElements];
   }
   // Wrapper around operator delete
   static void delete_CaloTemplatecLcLCorrelationParameter(void *p) {
      delete ((::CaloTemplate::CorrelationParameter*)p);
   }
   static void deleteArray_CaloTemplatecLcLCorrelationParameter(void *p) {
      delete [] ((::CaloTemplate::CorrelationParameter*)p);
   }
   static void destruct_CaloTemplatecLcLCorrelationParameter(void *p) {
      typedef ::CaloTemplate::CorrelationParameter current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class ::CaloTemplate::CorrelationParameter

namespace ROOT {
   static TClass *vectorlEvectorlEMuonTemplategRsPgR_Dictionary();
   static void vectorlEvectorlEMuonTemplategRsPgR_TClassManip(TClass*);
   static void *new_vectorlEvectorlEMuonTemplategRsPgR(void *p = 0);
   static void *newArray_vectorlEvectorlEMuonTemplategRsPgR(Long_t size, void *p);
   static void delete_vectorlEvectorlEMuonTemplategRsPgR(void *p);
   static void deleteArray_vectorlEvectorlEMuonTemplategRsPgR(void *p);
   static void destruct_vectorlEvectorlEMuonTemplategRsPgR(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const vector<vector<MuonTemplate> >*)
   {
      vector<vector<MuonTemplate> > *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TIsAProxy(typeid(vector<vector<MuonTemplate> >));
      static ::ROOT::TGenericClassInfo 
         instance("vector<vector<MuonTemplate> >", -2, "vector", 214,
                  typeid(vector<vector<MuonTemplate> >), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &vectorlEvectorlEMuonTemplategRsPgR_Dictionary, isa_proxy, 4,
                  sizeof(vector<vector<MuonTemplate> >) );
      instance.SetNew(&new_vectorlEvectorlEMuonTemplategRsPgR);
      instance.SetNewArray(&newArray_vectorlEvectorlEMuonTemplategRsPgR);
      instance.SetDelete(&delete_vectorlEvectorlEMuonTemplategRsPgR);
      instance.SetDeleteArray(&deleteArray_vectorlEvectorlEMuonTemplategRsPgR);
      instance.SetDestructor(&destruct_vectorlEvectorlEMuonTemplategRsPgR);
      instance.AdoptCollectionProxyInfo(TCollectionProxyInfo::Generate(TCollectionProxyInfo::Pushback< vector<vector<MuonTemplate> > >()));
      return &instance;
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_(Init) = GenerateInitInstanceLocal((const vector<vector<MuonTemplate> >*)0x0); R__UseDummy(_R__UNIQUE_(Init));

   // Dictionary for non-ClassDef classes
   static TClass *vectorlEvectorlEMuonTemplategRsPgR_Dictionary() {
      TClass* theClass =::ROOT::GenerateInitInstanceLocal((const vector<vector<MuonTemplate> >*)0x0)->GetClass();
      vectorlEvectorlEMuonTemplategRsPgR_TClassManip(theClass);
   return theClass;
   }

   static void vectorlEvectorlEMuonTemplategRsPgR_TClassManip(TClass* ){
   }

} // end of namespace ROOT

namespace ROOT {
   // Wrappers around operator new
   static void *new_vectorlEvectorlEMuonTemplategRsPgR(void *p) {
      return  p ? ::new((::ROOT::Internal::TOperatorNewHelper*)p) vector<vector<MuonTemplate> > : new vector<vector<MuonTemplate> >;
   }
   static void *newArray_vectorlEvectorlEMuonTemplategRsPgR(Long_t nElements, void *p) {
      return p ? ::new((::ROOT::Internal::TOperatorNewHelper*)p) vector<vector<MuonTemplate> >[nElements] : new vector<vector<MuonTemplate> >[nElements];
   }
   // Wrapper around operator delete
   static void delete_vectorlEvectorlEMuonTemplategRsPgR(void *p) {
      delete ((vector<vector<MuonTemplate> >*)p);
   }
   static void deleteArray_vectorlEvectorlEMuonTemplategRsPgR(void *p) {
      delete [] ((vector<vector<MuonTemplate> >*)p);
   }
   static void destruct_vectorlEvectorlEMuonTemplategRsPgR(void *p) {
      typedef vector<vector<MuonTemplate> > current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class vector<vector<MuonTemplate> >

namespace ROOT {
   static TClass *vectorlEvectorlECorrelationTemplategRsPgR_Dictionary();
   static void vectorlEvectorlECorrelationTemplategRsPgR_TClassManip(TClass*);
   static void *new_vectorlEvectorlECorrelationTemplategRsPgR(void *p = 0);
   static void *newArray_vectorlEvectorlECorrelationTemplategRsPgR(Long_t size, void *p);
   static void delete_vectorlEvectorlECorrelationTemplategRsPgR(void *p);
   static void deleteArray_vectorlEvectorlECorrelationTemplategRsPgR(void *p);
   static void destruct_vectorlEvectorlECorrelationTemplategRsPgR(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const vector<vector<CorrelationTemplate> >*)
   {
      vector<vector<CorrelationTemplate> > *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TIsAProxy(typeid(vector<vector<CorrelationTemplate> >));
      static ::ROOT::TGenericClassInfo 
         instance("vector<vector<CorrelationTemplate> >", -2, "vector", 214,
                  typeid(vector<vector<CorrelationTemplate> >), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &vectorlEvectorlECorrelationTemplategRsPgR_Dictionary, isa_proxy, 4,
                  sizeof(vector<vector<CorrelationTemplate> >) );
      instance.SetNew(&new_vectorlEvectorlECorrelationTemplategRsPgR);
      instance.SetNewArray(&newArray_vectorlEvectorlECorrelationTemplategRsPgR);
      instance.SetDelete(&delete_vectorlEvectorlECorrelationTemplategRsPgR);
      instance.SetDeleteArray(&deleteArray_vectorlEvectorlECorrelationTemplategRsPgR);
      instance.SetDestructor(&destruct_vectorlEvectorlECorrelationTemplategRsPgR);
      instance.AdoptCollectionProxyInfo(TCollectionProxyInfo::Generate(TCollectionProxyInfo::Pushback< vector<vector<CorrelationTemplate> > >()));
      return &instance;
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_(Init) = GenerateInitInstanceLocal((const vector<vector<CorrelationTemplate> >*)0x0); R__UseDummy(_R__UNIQUE_(Init));

   // Dictionary for non-ClassDef classes
   static TClass *vectorlEvectorlECorrelationTemplategRsPgR_Dictionary() {
      TClass* theClass =::ROOT::GenerateInitInstanceLocal((const vector<vector<CorrelationTemplate> >*)0x0)->GetClass();
      vectorlEvectorlECorrelationTemplategRsPgR_TClassManip(theClass);
   return theClass;
   }

   static void vectorlEvectorlECorrelationTemplategRsPgR_TClassManip(TClass* ){
   }

} // end of namespace ROOT

namespace ROOT {
   // Wrappers around operator new
   static void *new_vectorlEvectorlECorrelationTemplategRsPgR(void *p) {
      return  p ? ::new((::ROOT::Internal::TOperatorNewHelper*)p) vector<vector<CorrelationTemplate> > : new vector<vector<CorrelationTemplate> >;
   }
   static void *newArray_vectorlEvectorlECorrelationTemplategRsPgR(Long_t nElements, void *p) {
      return p ? ::new((::ROOT::Internal::TOperatorNewHelper*)p) vector<vector<CorrelationTemplate> >[nElements] : new vector<vector<CorrelationTemplate> >[nElements];
   }
   // Wrapper around operator delete
   static void delete_vectorlEvectorlECorrelationTemplategRsPgR(void *p) {
      delete ((vector<vector<CorrelationTemplate> >*)p);
   }
   static void deleteArray_vectorlEvectorlECorrelationTemplategRsPgR(void *p) {
      delete [] ((vector<vector<CorrelationTemplate> >*)p);
   }
   static void destruct_vectorlEvectorlECorrelationTemplategRsPgR(void *p) {
      typedef vector<vector<CorrelationTemplate> > current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class vector<vector<CorrelationTemplate> >

namespace ROOT {
   static TClass *vectorlEvectorlECaloTemplategRsPgR_Dictionary();
   static void vectorlEvectorlECaloTemplategRsPgR_TClassManip(TClass*);
   static void *new_vectorlEvectorlECaloTemplategRsPgR(void *p = 0);
   static void *newArray_vectorlEvectorlECaloTemplategRsPgR(Long_t size, void *p);
   static void delete_vectorlEvectorlECaloTemplategRsPgR(void *p);
   static void deleteArray_vectorlEvectorlECaloTemplategRsPgR(void *p);
   static void destruct_vectorlEvectorlECaloTemplategRsPgR(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const vector<vector<CaloTemplate> >*)
   {
      vector<vector<CaloTemplate> > *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TIsAProxy(typeid(vector<vector<CaloTemplate> >));
      static ::ROOT::TGenericClassInfo 
         instance("vector<vector<CaloTemplate> >", -2, "vector", 214,
                  typeid(vector<vector<CaloTemplate> >), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &vectorlEvectorlECaloTemplategRsPgR_Dictionary, isa_proxy, 4,
                  sizeof(vector<vector<CaloTemplate> >) );
      instance.SetNew(&new_vectorlEvectorlECaloTemplategRsPgR);
      instance.SetNewArray(&newArray_vectorlEvectorlECaloTemplategRsPgR);
      instance.SetDelete(&delete_vectorlEvectorlECaloTemplategRsPgR);
      instance.SetDeleteArray(&deleteArray_vectorlEvectorlECaloTemplategRsPgR);
      instance.SetDestructor(&destruct_vectorlEvectorlECaloTemplategRsPgR);
      instance.AdoptCollectionProxyInfo(TCollectionProxyInfo::Generate(TCollectionProxyInfo::Pushback< vector<vector<CaloTemplate> > >()));
      return &instance;
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_(Init) = GenerateInitInstanceLocal((const vector<vector<CaloTemplate> >*)0x0); R__UseDummy(_R__UNIQUE_(Init));

   // Dictionary for non-ClassDef classes
   static TClass *vectorlEvectorlECaloTemplategRsPgR_Dictionary() {
      TClass* theClass =::ROOT::GenerateInitInstanceLocal((const vector<vector<CaloTemplate> >*)0x0)->GetClass();
      vectorlEvectorlECaloTemplategRsPgR_TClassManip(theClass);
   return theClass;
   }

   static void vectorlEvectorlECaloTemplategRsPgR_TClassManip(TClass* ){
   }

} // end of namespace ROOT

namespace ROOT {
   // Wrappers around operator new
   static void *new_vectorlEvectorlECaloTemplategRsPgR(void *p) {
      return  p ? ::new((::ROOT::Internal::TOperatorNewHelper*)p) vector<vector<CaloTemplate> > : new vector<vector<CaloTemplate> >;
   }
   static void *newArray_vectorlEvectorlECaloTemplategRsPgR(Long_t nElements, void *p) {
      return p ? ::new((::ROOT::Internal::TOperatorNewHelper*)p) vector<vector<CaloTemplate> >[nElements] : new vector<vector<CaloTemplate> >[nElements];
   }
   // Wrapper around operator delete
   static void delete_vectorlEvectorlECaloTemplategRsPgR(void *p) {
      delete ((vector<vector<CaloTemplate> >*)p);
   }
   static void deleteArray_vectorlEvectorlECaloTemplategRsPgR(void *p) {
      delete [] ((vector<vector<CaloTemplate> >*)p);
   }
   static void destruct_vectorlEvectorlECaloTemplategRsPgR(void *p) {
      typedef vector<vector<CaloTemplate> > current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class vector<vector<CaloTemplate> >

namespace ROOT {
   static TClass *vectorlEMuonTemplategR_Dictionary();
   static void vectorlEMuonTemplategR_TClassManip(TClass*);
   static void *new_vectorlEMuonTemplategR(void *p = 0);
   static void *newArray_vectorlEMuonTemplategR(Long_t size, void *p);
   static void delete_vectorlEMuonTemplategR(void *p);
   static void deleteArray_vectorlEMuonTemplategR(void *p);
   static void destruct_vectorlEMuonTemplategR(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const vector<MuonTemplate>*)
   {
      vector<MuonTemplate> *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TIsAProxy(typeid(vector<MuonTemplate>));
      static ::ROOT::TGenericClassInfo 
         instance("vector<MuonTemplate>", -2, "vector", 214,
                  typeid(vector<MuonTemplate>), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &vectorlEMuonTemplategR_Dictionary, isa_proxy, 4,
                  sizeof(vector<MuonTemplate>) );
      instance.SetNew(&new_vectorlEMuonTemplategR);
      instance.SetNewArray(&newArray_vectorlEMuonTemplategR);
      instance.SetDelete(&delete_vectorlEMuonTemplategR);
      instance.SetDeleteArray(&deleteArray_vectorlEMuonTemplategR);
      instance.SetDestructor(&destruct_vectorlEMuonTemplategR);
      instance.AdoptCollectionProxyInfo(TCollectionProxyInfo::Generate(TCollectionProxyInfo::Pushback< vector<MuonTemplate> >()));
      return &instance;
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_(Init) = GenerateInitInstanceLocal((const vector<MuonTemplate>*)0x0); R__UseDummy(_R__UNIQUE_(Init));

   // Dictionary for non-ClassDef classes
   static TClass *vectorlEMuonTemplategR_Dictionary() {
      TClass* theClass =::ROOT::GenerateInitInstanceLocal((const vector<MuonTemplate>*)0x0)->GetClass();
      vectorlEMuonTemplategR_TClassManip(theClass);
   return theClass;
   }

   static void vectorlEMuonTemplategR_TClassManip(TClass* ){
   }

} // end of namespace ROOT

namespace ROOT {
   // Wrappers around operator new
   static void *new_vectorlEMuonTemplategR(void *p) {
      return  p ? ::new((::ROOT::Internal::TOperatorNewHelper*)p) vector<MuonTemplate> : new vector<MuonTemplate>;
   }
   static void *newArray_vectorlEMuonTemplategR(Long_t nElements, void *p) {
      return p ? ::new((::ROOT::Internal::TOperatorNewHelper*)p) vector<MuonTemplate>[nElements] : new vector<MuonTemplate>[nElements];
   }
   // Wrapper around operator delete
   static void delete_vectorlEMuonTemplategR(void *p) {
      delete ((vector<MuonTemplate>*)p);
   }
   static void deleteArray_vectorlEMuonTemplategR(void *p) {
      delete [] ((vector<MuonTemplate>*)p);
   }
   static void destruct_vectorlEMuonTemplategR(void *p) {
      typedef vector<MuonTemplate> current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class vector<MuonTemplate>

namespace ROOT {
   static TClass *vectorlEMuonTemplatecLcLObjectParametergR_Dictionary();
   static void vectorlEMuonTemplatecLcLObjectParametergR_TClassManip(TClass*);
   static void *new_vectorlEMuonTemplatecLcLObjectParametergR(void *p = 0);
   static void *newArray_vectorlEMuonTemplatecLcLObjectParametergR(Long_t size, void *p);
   static void delete_vectorlEMuonTemplatecLcLObjectParametergR(void *p);
   static void deleteArray_vectorlEMuonTemplatecLcLObjectParametergR(void *p);
   static void destruct_vectorlEMuonTemplatecLcLObjectParametergR(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const vector<MuonTemplate::ObjectParameter>*)
   {
      vector<MuonTemplate::ObjectParameter> *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TIsAProxy(typeid(vector<MuonTemplate::ObjectParameter>));
      static ::ROOT::TGenericClassInfo 
         instance("vector<MuonTemplate::ObjectParameter>", -2, "vector", 214,
                  typeid(vector<MuonTemplate::ObjectParameter>), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &vectorlEMuonTemplatecLcLObjectParametergR_Dictionary, isa_proxy, 4,
                  sizeof(vector<MuonTemplate::ObjectParameter>) );
      instance.SetNew(&new_vectorlEMuonTemplatecLcLObjectParametergR);
      instance.SetNewArray(&newArray_vectorlEMuonTemplatecLcLObjectParametergR);
      instance.SetDelete(&delete_vectorlEMuonTemplatecLcLObjectParametergR);
      instance.SetDeleteArray(&deleteArray_vectorlEMuonTemplatecLcLObjectParametergR);
      instance.SetDestructor(&destruct_vectorlEMuonTemplatecLcLObjectParametergR);
      instance.AdoptCollectionProxyInfo(TCollectionProxyInfo::Generate(TCollectionProxyInfo::Pushback< vector<MuonTemplate::ObjectParameter> >()));
      return &instance;
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_(Init) = GenerateInitInstanceLocal((const vector<MuonTemplate::ObjectParameter>*)0x0); R__UseDummy(_R__UNIQUE_(Init));

   // Dictionary for non-ClassDef classes
   static TClass *vectorlEMuonTemplatecLcLObjectParametergR_Dictionary() {
      TClass* theClass =::ROOT::GenerateInitInstanceLocal((const vector<MuonTemplate::ObjectParameter>*)0x0)->GetClass();
      vectorlEMuonTemplatecLcLObjectParametergR_TClassManip(theClass);
   return theClass;
   }

   static void vectorlEMuonTemplatecLcLObjectParametergR_TClassManip(TClass* ){
   }

} // end of namespace ROOT

namespace ROOT {
   // Wrappers around operator new
   static void *new_vectorlEMuonTemplatecLcLObjectParametergR(void *p) {
      return  p ? ::new((::ROOT::Internal::TOperatorNewHelper*)p) vector<MuonTemplate::ObjectParameter> : new vector<MuonTemplate::ObjectParameter>;
   }
   static void *newArray_vectorlEMuonTemplatecLcLObjectParametergR(Long_t nElements, void *p) {
      return p ? ::new((::ROOT::Internal::TOperatorNewHelper*)p) vector<MuonTemplate::ObjectParameter>[nElements] : new vector<MuonTemplate::ObjectParameter>[nElements];
   }
   // Wrapper around operator delete
   static void delete_vectorlEMuonTemplatecLcLObjectParametergR(void *p) {
      delete ((vector<MuonTemplate::ObjectParameter>*)p);
   }
   static void deleteArray_vectorlEMuonTemplatecLcLObjectParametergR(void *p) {
      delete [] ((vector<MuonTemplate::ObjectParameter>*)p);
   }
   static void destruct_vectorlEMuonTemplatecLcLObjectParametergR(void *p) {
      typedef vector<MuonTemplate::ObjectParameter> current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class vector<MuonTemplate::ObjectParameter>

namespace ROOT {
   static TClass *vectorlECorrelationTemplategR_Dictionary();
   static void vectorlECorrelationTemplategR_TClassManip(TClass*);
   static void *new_vectorlECorrelationTemplategR(void *p = 0);
   static void *newArray_vectorlECorrelationTemplategR(Long_t size, void *p);
   static void delete_vectorlECorrelationTemplategR(void *p);
   static void deleteArray_vectorlECorrelationTemplategR(void *p);
   static void destruct_vectorlECorrelationTemplategR(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const vector<CorrelationTemplate>*)
   {
      vector<CorrelationTemplate> *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TIsAProxy(typeid(vector<CorrelationTemplate>));
      static ::ROOT::TGenericClassInfo 
         instance("vector<CorrelationTemplate>", -2, "vector", 214,
                  typeid(vector<CorrelationTemplate>), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &vectorlECorrelationTemplategR_Dictionary, isa_proxy, 4,
                  sizeof(vector<CorrelationTemplate>) );
      instance.SetNew(&new_vectorlECorrelationTemplategR);
      instance.SetNewArray(&newArray_vectorlECorrelationTemplategR);
      instance.SetDelete(&delete_vectorlECorrelationTemplategR);
      instance.SetDeleteArray(&deleteArray_vectorlECorrelationTemplategR);
      instance.SetDestructor(&destruct_vectorlECorrelationTemplategR);
      instance.AdoptCollectionProxyInfo(TCollectionProxyInfo::Generate(TCollectionProxyInfo::Pushback< vector<CorrelationTemplate> >()));
      return &instance;
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_(Init) = GenerateInitInstanceLocal((const vector<CorrelationTemplate>*)0x0); R__UseDummy(_R__UNIQUE_(Init));

   // Dictionary for non-ClassDef classes
   static TClass *vectorlECorrelationTemplategR_Dictionary() {
      TClass* theClass =::ROOT::GenerateInitInstanceLocal((const vector<CorrelationTemplate>*)0x0)->GetClass();
      vectorlECorrelationTemplategR_TClassManip(theClass);
   return theClass;
   }

   static void vectorlECorrelationTemplategR_TClassManip(TClass* ){
   }

} // end of namespace ROOT

namespace ROOT {
   // Wrappers around operator new
   static void *new_vectorlECorrelationTemplategR(void *p) {
      return  p ? ::new((::ROOT::Internal::TOperatorNewHelper*)p) vector<CorrelationTemplate> : new vector<CorrelationTemplate>;
   }
   static void *newArray_vectorlECorrelationTemplategR(Long_t nElements, void *p) {
      return p ? ::new((::ROOT::Internal::TOperatorNewHelper*)p) vector<CorrelationTemplate>[nElements] : new vector<CorrelationTemplate>[nElements];
   }
   // Wrapper around operator delete
   static void delete_vectorlECorrelationTemplategR(void *p) {
      delete ((vector<CorrelationTemplate>*)p);
   }
   static void deleteArray_vectorlECorrelationTemplategR(void *p) {
      delete [] ((vector<CorrelationTemplate>*)p);
   }
   static void destruct_vectorlECorrelationTemplategR(void *p) {
      typedef vector<CorrelationTemplate> current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class vector<CorrelationTemplate>

namespace ROOT {
   static TClass *vectorlECaloTemplategR_Dictionary();
   static void vectorlECaloTemplategR_TClassManip(TClass*);
   static void *new_vectorlECaloTemplategR(void *p = 0);
   static void *newArray_vectorlECaloTemplategR(Long_t size, void *p);
   static void delete_vectorlECaloTemplategR(void *p);
   static void deleteArray_vectorlECaloTemplategR(void *p);
   static void destruct_vectorlECaloTemplategR(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const vector<CaloTemplate>*)
   {
      vector<CaloTemplate> *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TIsAProxy(typeid(vector<CaloTemplate>));
      static ::ROOT::TGenericClassInfo 
         instance("vector<CaloTemplate>", -2, "vector", 214,
                  typeid(vector<CaloTemplate>), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &vectorlECaloTemplategR_Dictionary, isa_proxy, 4,
                  sizeof(vector<CaloTemplate>) );
      instance.SetNew(&new_vectorlECaloTemplategR);
      instance.SetNewArray(&newArray_vectorlECaloTemplategR);
      instance.SetDelete(&delete_vectorlECaloTemplategR);
      instance.SetDeleteArray(&deleteArray_vectorlECaloTemplategR);
      instance.SetDestructor(&destruct_vectorlECaloTemplategR);
      instance.AdoptCollectionProxyInfo(TCollectionProxyInfo::Generate(TCollectionProxyInfo::Pushback< vector<CaloTemplate> >()));
      return &instance;
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_(Init) = GenerateInitInstanceLocal((const vector<CaloTemplate>*)0x0); R__UseDummy(_R__UNIQUE_(Init));

   // Dictionary for non-ClassDef classes
   static TClass *vectorlECaloTemplategR_Dictionary() {
      TClass* theClass =::ROOT::GenerateInitInstanceLocal((const vector<CaloTemplate>*)0x0)->GetClass();
      vectorlECaloTemplategR_TClassManip(theClass);
   return theClass;
   }

   static void vectorlECaloTemplategR_TClassManip(TClass* ){
   }

} // end of namespace ROOT

namespace ROOT {
   // Wrappers around operator new
   static void *new_vectorlECaloTemplategR(void *p) {
      return  p ? ::new((::ROOT::Internal::TOperatorNewHelper*)p) vector<CaloTemplate> : new vector<CaloTemplate>;
   }
   static void *newArray_vectorlECaloTemplategR(Long_t nElements, void *p) {
      return p ? ::new((::ROOT::Internal::TOperatorNewHelper*)p) vector<CaloTemplate>[nElements] : new vector<CaloTemplate>[nElements];
   }
   // Wrapper around operator delete
   static void delete_vectorlECaloTemplategR(void *p) {
      delete ((vector<CaloTemplate>*)p);
   }
   static void deleteArray_vectorlECaloTemplategR(void *p) {
      delete [] ((vector<CaloTemplate>*)p);
   }
   static void destruct_vectorlECaloTemplategR(void *p) {
      typedef vector<CaloTemplate> current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class vector<CaloTemplate>

namespace ROOT {
   static TClass *vectorlECaloTemplatecLcLObjectParametergR_Dictionary();
   static void vectorlECaloTemplatecLcLObjectParametergR_TClassManip(TClass*);
   static void *new_vectorlECaloTemplatecLcLObjectParametergR(void *p = 0);
   static void *newArray_vectorlECaloTemplatecLcLObjectParametergR(Long_t size, void *p);
   static void delete_vectorlECaloTemplatecLcLObjectParametergR(void *p);
   static void deleteArray_vectorlECaloTemplatecLcLObjectParametergR(void *p);
   static void destruct_vectorlECaloTemplatecLcLObjectParametergR(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const vector<CaloTemplate::ObjectParameter>*)
   {
      vector<CaloTemplate::ObjectParameter> *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TIsAProxy(typeid(vector<CaloTemplate::ObjectParameter>));
      static ::ROOT::TGenericClassInfo 
         instance("vector<CaloTemplate::ObjectParameter>", -2, "vector", 214,
                  typeid(vector<CaloTemplate::ObjectParameter>), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &vectorlECaloTemplatecLcLObjectParametergR_Dictionary, isa_proxy, 4,
                  sizeof(vector<CaloTemplate::ObjectParameter>) );
      instance.SetNew(&new_vectorlECaloTemplatecLcLObjectParametergR);
      instance.SetNewArray(&newArray_vectorlECaloTemplatecLcLObjectParametergR);
      instance.SetDelete(&delete_vectorlECaloTemplatecLcLObjectParametergR);
      instance.SetDeleteArray(&deleteArray_vectorlECaloTemplatecLcLObjectParametergR);
      instance.SetDestructor(&destruct_vectorlECaloTemplatecLcLObjectParametergR);
      instance.AdoptCollectionProxyInfo(TCollectionProxyInfo::Generate(TCollectionProxyInfo::Pushback< vector<CaloTemplate::ObjectParameter> >()));
      return &instance;
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_(Init) = GenerateInitInstanceLocal((const vector<CaloTemplate::ObjectParameter>*)0x0); R__UseDummy(_R__UNIQUE_(Init));

   // Dictionary for non-ClassDef classes
   static TClass *vectorlECaloTemplatecLcLObjectParametergR_Dictionary() {
      TClass* theClass =::ROOT::GenerateInitInstanceLocal((const vector<CaloTemplate::ObjectParameter>*)0x0)->GetClass();
      vectorlECaloTemplatecLcLObjectParametergR_TClassManip(theClass);
   return theClass;
   }

   static void vectorlECaloTemplatecLcLObjectParametergR_TClassManip(TClass* ){
   }

} // end of namespace ROOT

namespace ROOT {
   // Wrappers around operator new
   static void *new_vectorlECaloTemplatecLcLObjectParametergR(void *p) {
      return  p ? ::new((::ROOT::Internal::TOperatorNewHelper*)p) vector<CaloTemplate::ObjectParameter> : new vector<CaloTemplate::ObjectParameter>;
   }
   static void *newArray_vectorlECaloTemplatecLcLObjectParametergR(Long_t nElements, void *p) {
      return p ? ::new((::ROOT::Internal::TOperatorNewHelper*)p) vector<CaloTemplate::ObjectParameter>[nElements] : new vector<CaloTemplate::ObjectParameter>[nElements];
   }
   // Wrapper around operator delete
   static void delete_vectorlECaloTemplatecLcLObjectParametergR(void *p) {
      delete ((vector<CaloTemplate::ObjectParameter>*)p);
   }
   static void deleteArray_vectorlECaloTemplatecLcLObjectParametergR(void *p) {
      delete [] ((vector<CaloTemplate::ObjectParameter>*)p);
   }
   static void destruct_vectorlECaloTemplatecLcLObjectParametergR(void *p) {
      typedef vector<CaloTemplate::ObjectParameter> current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class vector<CaloTemplate::ObjectParameter>

namespace {
  void TriggerDictionaryInitialization_L1TriggerL1TGlobal_xr_Impl() {
    static const char* headers[] = {
0    };
    static const char* includePaths[] = {
"/afs/cern.ch/user/l/lkang/diphoton/rate_tests/CMSSW_8_0_11/src",
"/cvmfs/cms.cern.ch/slc6_amd64_gcc530/cms/cmssw/CMSSW_8_0_11/src",
"/cvmfs/cms.cern.ch/slc6_amd64_gcc530/lcg/root/6.06.00-ikhhed4/include",
"/cvmfs/cms.cern.ch/slc6_amd64_gcc530/external/boost/1.57.0-ikhhed/include",
"/cvmfs/cms.cern.ch/slc6_amd64_gcc530/external/pcre/8.37/include",
"/cvmfs/cms.cern.ch/slc6_amd64_gcc530/external/bz2lib/1.0.6/include",
"/cvmfs/cms.cern.ch/slc6_amd64_gcc530/external/gsl/1.16/include",
"/cvmfs/cms.cern.ch/slc6_amd64_gcc530/external/libuuid/2.22.2/include",
"/cvmfs/cms.cern.ch/slc6_amd64_gcc530/external/python/2.7.11-ikhhed/include/python2.7",
"/cvmfs/cms.cern.ch/slc6_amd64_gcc530/external/tbb/44_20151115oss/include",
"/cvmfs/cms.cern.ch/slc6_amd64_gcc530/external/xerces-c/2.8.0/include",
"/cvmfs/cms.cern.ch/slc6_amd64_gcc530/external/zlib/1.2.8/include",
"/cvmfs/cms.cern.ch/slc6_amd64_gcc530/lcg/root/6.06.00-ikhhed4/include",
"/afs/cern.ch/user/l/lkang/diphoton/rate_tests/CMSSW_8_0_11/",
0
    };
    static const char* fwdDeclCode = R"DICTFWDDCLS(
#line 1 "L1TriggerL1TGlobal_xr dictionary forward declarations' payload"
#pragma clang diagnostic ignored "-Wkeyword-compat"
#pragma clang diagnostic ignored "-Wignored-attributes"
#pragma clang diagnostic ignored "-Wreturn-type-c-linkage"
extern int __Cling_Autoloading_Map;
class __attribute__((annotate("$clingAutoload$L1Trigger/L1TGlobal/interface/TriggerMenu.h")))  CorrelationTemplate;
namespace std{template <typename _Tp> class __attribute__((annotate("$clingAutoload$string")))  allocator;
}
class __attribute__((annotate(R"ATTRDUMP(class_version@@@TriggerMenu_V01)ATTRDUMP"))) __attribute__((annotate("$clingAutoload$L1Trigger/L1TGlobal/interface/TriggerMenu.h")))  TriggerMenu;
class __attribute__((annotate("$clingAutoload$L1Trigger/L1TGlobal/interface/TriggerMenu.h")))  MuonTemplate;
class __attribute__((annotate("$clingAutoload$L1Trigger/L1TGlobal/interface/TriggerMenu.h")))  CaloTemplate;
)DICTFWDDCLS";
    static const char* payloadCode = R"DICTPAYLOAD(
#line 1 "L1TriggerL1TGlobal_xr dictionary payload"

#ifndef G__VECTOR_HAS_CLASS_ITERATOR
  #define G__VECTOR_HAS_CLASS_ITERATOR 1
#endif
#ifndef CMS_DICT_IMPL
  #define CMS_DICT_IMPL 1
#endif
#ifndef _REENTRANT
  #define _REENTRANT 1
#endif
#ifndef GNUSOURCE
  #define GNUSOURCE 1
#endif
#ifndef __STRICT_ANSI__
  #define __STRICT_ANSI__ 1
#endif
#ifndef GNU_GCC
  #define GNU_GCC 1
#endif
#ifndef _GNU_SOURCE
  #define _GNU_SOURCE 1
#endif
#ifndef CMSSW_GIT_HASH
  #define CMSSW_GIT_HASH "CMSSW_8_0_11"
#endif
#ifndef PROJECT_NAME
  #define PROJECT_NAME "CMSSW"
#endif
#ifndef PROJECT_VERSION
  #define PROJECT_VERSION "CMSSW_8_0_11"
#endif
#ifndef BOOST_SPIRIT_THREADSAFE
  #define BOOST_SPIRIT_THREADSAFE 1
#endif
#ifndef PHOENIX_THREADSAFE
  #define PHOENIX_THREADSAFE 1
#endif
#ifndef CMSSW_REFLEX_DICT
  #define CMSSW_REFLEX_DICT 1
#endif

#define _BACKWARD_BACKWARD_WARNING_H
#include "L1Trigger/L1TGlobal/interface/GlobalCondition.h"
#include "L1Trigger/L1TGlobal/interface/TriggerMenu.h"

namespace L1Trigger_L1TGlobal {
  struct dictionary {
    std::vector<MuonTemplate> dummy1 ;
    std::vector<CaloTemplate> dummy2 ;
    std::vector<CorrelationTemplate> dummy3 ;
  };
}

#undef  _BACKWARD_BACKWARD_WARNING_H
)DICTPAYLOAD";
    static const char* classesHeaders[]={
"CaloTemplate", payloadCode, "@",
"CaloTemplate::CorrelationParameter", payloadCode, "@",
"CaloTemplate::ObjectParameter", payloadCode, "@",
"CorrelationTemplate", payloadCode, "@",
"CorrelationTemplate::CorrelationParameter", payloadCode, "@",
"MuonTemplate", payloadCode, "@",
"MuonTemplate::CorrelationParameter", payloadCode, "@",
"MuonTemplate::ObjectParameter", payloadCode, "@",
"TriggerMenu", payloadCode, "@",
nullptr};

    static bool isInitialized = false;
    if (!isInitialized) {
      TROOT::RegisterModule("L1TriggerL1TGlobal_xr",
        headers, includePaths, payloadCode, fwdDeclCode,
        TriggerDictionaryInitialization_L1TriggerL1TGlobal_xr_Impl, {}, classesHeaders);
      isInitialized = true;
    }
  }
  static struct DictInit {
    DictInit() {
      TriggerDictionaryInitialization_L1TriggerL1TGlobal_xr_Impl();
    }
  } __TheDictionaryInitializer;
}
void TriggerDictionaryInitialization_L1TriggerL1TGlobal_xr() {
  TriggerDictionaryInitialization_L1TriggerL1TGlobal_xr_Impl();
}
