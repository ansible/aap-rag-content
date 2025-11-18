#!/bin/bash
if [[ "${LLAMA_STACK_CONFIG_DIR}" == "" ]]; then
  echo "Environment variable LLAMA_STACK_CONFIG_DIR is not defined."
  exit 1
fi

echo "Initialize RAG vector database"
if [[ ! -d ${LLAMA_STACK_CONFIG_DIR} ]]; then
  echo "Volume mount path is not found."
  exit 1
fi

DESTDIR=${LLAMA_STACK_CONFIG_DIR}/distributions/ansible-chatbot
mkdir -p ${DESTDIR}
cd /rag/llama_stack_vector_db

diff faiss_store.db.gz.sha256 ${DESTDIR}/faiss_store.db.gz.sha256
if [[ $? != 0 ]]; then
  gzip -cd faiss_store.db.gz > ${DESTDIR}/aap_faiss_store.db
  if [[ $? != 0 ]]; then
    echo "Failed to install new vector database file."
    exit 1
  fi
  cp faiss_store.db.gz.sha256 ${DESTDIR}
  echo "Latest vector database file has been installed."
else
  echo "Latest vector database file already up-to-date and installed."
fi

ls -l ${DESTDIR}/aap_faiss_store.db
cat ${DESTDIR}/faiss_store.db.gz.sha256

echo "Initialize RAG environment variables"
cd /rag/llama_stack_vector_db
diff provider_vector_db_id.ind ${DESTDIR}/provider_vector_db_id.ind
if [[ $? != 0 ]]; then
  cp provider_vector_db_id.ind ${DESTDIR}
  echo -e "PROVIDER_VECTOR_DB_ID=$(cat provider_vector_db_id.ind)" > ${DESTDIR}/provider_rag.env
  echo "RAG environment variables updated."
else
  echo "RAG environment variables already up-to-date."
fi

cat ${DESTDIR}/provider_rag.env
echo ""

echo "Initialize embedding model"
cd /rag
diff embeddings_model/config.json ${LLAMA_STACK_CONFIG_DIR}/embeddings_model/config.json
if [[ $? != 0 ]]; then
  rm -rf ${LLAMA_STACK_CONFIG_DIR}/embeddings_model
  cp -r embeddings_model ${LLAMA_STACK_CONFIG_DIR}
  if [[ $? != 0 ]]; then
    echo "Failed to install embedding model."
    exit 1
  fi
  echo "Latest embeddings model has been installed."
else
  echo "Latest embeddings model already up-to-date and installed."
fi

cat ${LLAMA_STACK_CONFIG_DIR}/embeddings_model/config.json
